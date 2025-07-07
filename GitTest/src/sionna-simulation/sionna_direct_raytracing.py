#!/usr/bin/env python3
"""
Direct Sionna Ray Tracing with Built-in Scene
=============================================

This script demonstrates Sionna ray tracing using built-in scenes
and your dummy AP coordinates.
"""

import os
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from PIL import Image
import csv

# Import Sionna modules
import sionna
from sionna.rt import load_scene, Transmitter, PlanarArray, Camera

def load_transmitters_from_csv(filename):
    """Load transmitters from CSV file."""
    transmitters = []
    print(f"📡 Loading transmitters from: {filename}")
    
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        # Skip header if present
        first_row = next(reader)
        if not (first_row[0].replace('.','').replace('-','').isdigit()):
            # Has header, continue with next rows
            pass
        else:
            # No header, process first row
            name, x, y, z = first_row
            transmitters.append((name, [float(x), float(y), float(z)]))
        
        # Process remaining rows
        for row in reader:
            if len(row) >= 4:
                name, x, y, z = row[:4]
                transmitters.append((name, [float(x), float(y), float(z)]))
                print(f"   📍 {name}: ({x}, {y}, {z})")
    
    print(f"✅ Loaded {len(transmitters)} transmitters")
    return transmitters

def create_sionna_scene_with_dummy_aps():
    """Create a Sionna scene with dummy APs."""
    print("🏗️ Creating Sionna scene...")
    
    # Try to load a built-in scene or create a simple one
    try:
        # Load a simple built-in scene
        scene = load_scene(sionna.rt.scene.simple_wedge)
        print("✅ Loaded simple wedge scene")
    except:
        try:
            # Try alternative scene
            scene = load_scene(sionna.rt.scene.simple_street_canyon)
            print("✅ Loaded simple street canyon scene")
        except:
            print("❌ Could not load built-in scenes, creating minimal scene...")
            # Create a minimal scene programmatically
            from sionna.rt import Scene
            scene = Scene()
    
    # Set frequency
    scene.frequency = 2.4e9  # 2.4 GHz
    
    return scene

def run_coverage_simulation():
    """Run the coverage simulation."""
    print("🚀 SIONNA RAY TRACING WITH DUMMY APs")
    print("====================================")
    
    # Load dummy AP coordinates
    ap_file = "/home/sionna/Documents/GitTest/src/data/2f.csv"
    if not os.path.exists(ap_file):
        print(f"❌ AP file not found: {ap_file}")
        return False
    
    transmitters = load_transmitters_from_csv(ap_file)
    
    if not transmitters:
        print("❌ No transmitters loaded")
        return False
    
    # Create scene
    scene = create_sionna_scene_with_dummy_aps()
    
    # Add transmitters to scene
    print("📡 Adding transmitters to scene...")
    for i, (name, position) in enumerate(transmitters):
        # Create transmitter
        tx = Transmitter(name=f"AP_{i+1}", 
                        position=position)
        scene.add(tx)
        print(f"   ✅ Added {name} at {position}")
    
    print(f"✅ Scene ready with {len(transmitters)} access points")
    
    # Set up camera for coverage computation
    print("📷 Setting up coverage computation...")
    
    # Create camera at reasonable height looking down
    camera = Camera(name="coverage_camera",
                   position=[20, 30, 8],  # Position above the APs
                   look_at=[20, 30, 0],   # Look down at ground level
                   up=[0, 1, 0])          # Up vector
    scene.add(camera)
    
    # Compute coverage map
    print("🎯 Computing coverage map (this may take a few minutes)...")
    
    try:
        # Compute coverage
        coverage_map = scene.coverage_map(num_samples=int(1e6),
                                        resolution=[200, 200],
                                        cm_center=[20, 30, 1.5],  # Center at reasonable height
                                        cm_orientation=[0, 0, 0],
                                        cm_size=[40, 40])
        
        print("✅ Coverage computation completed")
        
        # Save coverage map
        output_dir = "/home/sionna/Documents/GitTest/src/sionna-simulation/sionna_direct_results"
        os.makedirs(output_dir, exist_ok=True)
        
        # Convert to image and save
        coverage_db = 10 * np.log10(coverage_map.numpy())
        
        # Create visualization
        plt.figure(figsize=(12, 10))
        plt.imshow(coverage_db.squeeze(), cmap='viridis', origin='lower')
        plt.colorbar(label='Path Gain (dB)')
        plt.title('WiFi Coverage Map - Sionna Ray Tracing\nDummy APs in Building Scene')
        plt.xlabel('X Position')
        plt.ylabel('Y Position')
        
        # Add AP positions to plot
        for i, (name, pos) in enumerate(transmitters):
            plt.plot(pos[0]*5, pos[1]*5, 'r*', markersize=15, label=f'AP {i+1}' if i < 3 else "")
        
        if len(transmitters) <= 3:
            plt.legend()
        
        # Save plot
        plot_file = os.path.join(output_dir, "sionna_coverage_raytracing.png")
        plt.savefig(plot_file, dpi=300, bbox_inches='tight')
        plt.close()
        
        # Save raw data
        np.save(os.path.join(output_dir, "coverage_data.npy"), coverage_map.numpy())
        
        print(f"💾 Results saved to: {output_dir}")
        print(f"   📊 Coverage map: {plot_file}")
        print(f"   📄 Raw data: coverage_data.npy")
        
        # Generate summary
        coverage_linear = coverage_map.numpy()
        coverage_db_vals = 10 * np.log10(coverage_linear[coverage_linear > 0])
        
        print(f"\n📈 Coverage Statistics:")
        print(f"   📊 Mean signal: {np.mean(coverage_db_vals):.1f} dB")
        print(f"   📊 Max signal: {np.max(coverage_db_vals):.1f} dB")
        print(f"   📊 Min signal: {np.min(coverage_db_vals):.1f} dB")
        print(f"   📊 Coverage area: {np.sum(coverage_linear > 1e-10) / coverage_linear.size * 100:.1f}%")
        
        return True
        
    except Exception as e:
        print(f"❌ Error during coverage computation: {e}")
        return False

if __name__ == "__main__":
    success = run_coverage_simulation()
    
    if success:
        print("\n🎉 SIONNA RAY TRACING COMPLETE!")
        print("===============================")
        print("✅ Full ray tracing simulation completed successfully")
        print("📡 Dummy APs integrated with Sionna scene")
        print("🎯 Realistic coverage analysis generated")
    else:
        print("\n❌ Simulation failed")
        print("Check error messages above for troubleshooting")
