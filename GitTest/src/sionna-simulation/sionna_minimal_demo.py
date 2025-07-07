#!/usr/bin/env python3
"""
Minimal Sionna Ray Tracing Demo
==============================

Simple demonstration of Sionna ray tracing with dummy APs.
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import csv

# Sionna imports  
import sionna
from sionna.rt import load_scene, Transmitter

def load_dummy_aps():
    """Load dummy AP coordinates."""
    ap_file = "/home/sionna/Documents/GitTest/src/data/2f.csv"
    aps = []
    
    print(f"📡 Loading APs from: {ap_file}")
    with open(ap_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) >= 4:
                name, x, y, z = row[:4]
                aps.append((name, [float(x), float(y), float(z)]))
                print(f"   📍 {name}: ({x}, {y}, {z})")
    
    return aps

def main():
    print("🚀 MINIMAL SIONNA RAY TRACING DEMO")
    print("==================================")
    
    # Load built-in scene
    try:
        print("🏗️ Loading Sionna built-in scene...")
        scene = load_scene("simple_wedge")
        print("✅ Scene loaded successfully")
    except Exception as e:
        print(f"❌ Failed to load scene: {e}")
        return
    
    # Set frequency
    scene.frequency = 2.4e9
    print("📡 Set frequency to 2.4 GHz")
    
    # Load and add transmitters
    aps = load_dummy_aps()
    for i, (name, pos) in enumerate(aps):
        tx = Transmitter(name=f"AP_{i+1}", position=pos)
        scene.add(tx)
        print(f"✅ Added {name} to scene")
    
    print(f"\n📊 Scene Summary:")
    print(f"   🏗️ Scene: Simple wedge (built-in)")
    print(f"   📡 Transmitters: {len(aps)}")
    print(f"   📶 Frequency: 2.4 GHz")
    
    # Simple coverage computation
    print("\n🎯 Computing basic coverage...")
    try:
        # Use simpler coverage map computation
        coverage_map = scene.coverage_map(num_samples=100000,
                                        resolution=[100, 100])
        
        print("✅ Coverage computed successfully")
        
        # Save results
        output_dir = "/home/sionna/Documents/GitTest/src/sionna-simulation/sionna_minimal_demo"
        os.makedirs(output_dir, exist_ok=True)
        
        # Convert to dB and visualize
        coverage_linear = coverage_map.numpy().squeeze()
        coverage_db = 10 * np.log10(np.maximum(coverage_linear, 1e-12))
        
        # Create plot
        plt.figure(figsize=(10, 8))
        plt.imshow(coverage_db, cmap='viridis', origin='lower')
        plt.colorbar(label='Path Gain (dB)')
        plt.title('Sionna Ray Tracing Coverage Map\nDummy WiFi APs')
        plt.xlabel('X Grid Points')
        plt.ylabel('Y Grid Points')
        
        # Save
        plot_file = os.path.join(output_dir, "minimal_coverage_demo.png")
        plt.savefig(plot_file, dpi=200, bbox_inches='tight')
        plt.close()
        
        # Save data
        np.save(os.path.join(output_dir, "coverage_data.npy"), coverage_linear)
        
        # Statistics
        valid_coverage = coverage_db[coverage_db > -100]
        print(f"\n📈 Coverage Statistics:")
        print(f"   📊 Mean: {np.mean(valid_coverage):.1f} dB")
        print(f"   📊 Max: {np.max(valid_coverage):.1f} dB")
        print(f"   📊 Min: {np.min(valid_coverage):.1f} dB")
        
        print(f"\n💾 Results saved to: {output_dir}")
        print(f"   📊 Plot: {plot_file}")
        print(f"   📄 Data: coverage_data.npy")
        
        print(f"\n🎉 SIONNA RAY TRACING DEMO COMPLETE!")
        print("✅ Successfully demonstrated Sionna with dummy APs")
        
    except Exception as e:
        print(f"❌ Coverage computation failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
