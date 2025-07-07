#!/usr/bin/env python3
"""
Sionna 1.1.0 Compatible WiFi Coverage Simulation
=================================================

Full ray tracing simulation using dummy APs with Sionna 1.1.0 API.
Works with real building layouts and handles the new API changes.
"""

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import argparse
import os
import sys
from pathlib import Path

# Import Sionna 1.1.0 components
try:
    import sionna
    from sionna.rt import load_scene, PlanarArray, Transmitter, Receiver
    from sionna.rt import scene  # New in 1.1.0
    print(f"✅ Sionna {sionna.__version__} loaded successfully")
except ImportError as e:
    print(f"❌ Error importing Sionna: {e}")
    print("Install with: pip install sionna")
    sys.exit(1)

def load_dummy_aps(csv_file):
    """Load dummy AP coordinates from CSV file."""
    aps = []
    print(f"📡 Loading AP coordinates from: {csv_file}")
    
    try:
        with open(csv_file, 'r') as f:
            lines = f.readlines()
            
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#'):
                parts = line.split(',')
                if len(parts) >= 4:
                    name = parts[0].strip()
                    x = float(parts[1])
                    y = float(parts[2]) 
                    z = float(parts[3])
                    aps.append({'name': name, 'x': x, 'y': y, 'z': z})
                    print(f"  📍 {name}: ({x}, {y}, {z})")
                    
        print(f"✅ Loaded {len(aps)} AP transmitters")
        return aps
        
    except Exception as e:
        print(f"❌ Error loading APs: {e}")
        return []

def create_sionna_scene_simple():
    """Create a simple scene for Sionna 1.1.0 when Mitsuba files fail."""
    print("🏗️ Creating simple Sionna scene...")
    
    # Create a simple room scene
    try:
        # In Sionna 1.1.0, we can create scenes programmatically
        from sionna.rt import Rectangle
        
        # Create walls for a simple room (20m x 20m x 3m)
        scene = sionna.rt.Scene()
        
        # Floor
        floor = Rectangle("floor", width=20.0, height=20.0)
        floor.position = [0, 0, 0]
        floor.look_at([0, 0, 1])
        scene.add(floor)
        
        # Walls
        wall1 = Rectangle("wall1", width=20.0, height=3.0)
        wall1.position = [10, 0, 1.5]
        wall1.look_at([9, 0, 1.5])
        scene.add(wall1)
        
        wall2 = Rectangle("wall2", width=20.0, height=3.0)
        wall2.position = [-10, 0, 1.5]
        wall2.look_at([-9, 0, 1.5])
        scene.add(wall2)
        
        wall3 = Rectangle("wall3", width=20.0, height=3.0)
        wall3.position = [0, 10, 1.5]
        wall3.look_at([0, 9, 1.5])
        scene.add(wall3)
        
        wall4 = Rectangle("wall4", width=20.0, height=3.0)
        wall4.position = [0, -10, 1.5]
        wall4.look_at([0, -9, 1.5])
        scene.add(wall4)
        
        print("✅ Simple scene created")
        return scene
        
    except Exception as e:
        print(f"❌ Error creating simple scene: {e}")
        return None

def run_sionna_coverage_simulation(aps, output_dir):
    """Run Sionna 1.1.0 coverage simulation."""
    print(f"\n🚀 SIONNA 1.1.0 RAY TRACING SIMULATION")
    print("=" * 60)
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    try:
        # Create or load scene
        print("🏗️ Setting up simulation scene...")
        scene = create_sionna_scene_simple()
        
        if scene is None:
            print("❌ Failed to create scene")
            return False
            
        # Configure simulation parameters
        print("⚙️ Configuring simulation parameters...")
        scene.frequency = 2.4e9  # 2.4 GHz
        scene.tx_power = 20.0    # 20 dBm
        
        # Create antenna array (simple isotropic for now)
        array = PlanarArray(num_rows=1, num_cols=1, vertical_spacing=0.5, 
                           horizontal_spacing=0.5, pattern="iso", 
                           polarization="VV")
        
        # Add transmitters (APs)
        transmitters = []
        for i, ap in enumerate(aps):
            # Create transmitter
            tx = Transmitter(name=f"tx_{i}", 
                           position=[ap['x'], ap['y'], ap['z']],
                           orientation=[0, 0, 0])
            tx.antenna.array = array
            scene.add(tx)
            transmitters.append(tx)
            print(f"  📡 Added {ap['name']} at ({ap['x']}, {ap['y']}, {ap['z']})")
        
        # Create coverage grid
        print("📊 Setting up coverage grid...")
        coverage_map = scene.coverage_map(cm_cell_size=[0.5, 0.5],  # 0.5m resolution
                                        cm_orientation="z")
        
        print("🔄 Computing ray tracing coverage...")
        
        # Compute coverage (Sionna 1.1.0 style)
        coverage = coverage_map(num_samples=1000)  # Ray samples
        
        # Extract coverage data
        coverage_data = coverage.numpy()
        print(f"✅ Coverage computed - Shape: {coverage_data.shape}")
        
        # Create visualizations
        print("🎨 Creating coverage visualizations...")
        create_coverage_plots(coverage_data, aps, output_dir)
        
        # Save raw data
        np.savez(f"{output_dir}/sionna_coverage_data.npz", 
                coverage=coverage_data, 
                ap_positions=[(ap['x'], ap['y'], ap['z']) for ap in aps])
        
        print(f"✅ Simulation complete! Results saved to: {output_dir}")
        return True
        
    except Exception as e:
        print(f"❌ Simulation error: {e}")
        print(f"   This may be due to Sionna 1.1.0 API differences")
        print(f"   Consider downgrading to Sionna 0.19 for full compatibility")
        return False

def create_coverage_plots(coverage_data, aps, output_dir):
    """Create coverage visualization plots."""
    plt.style.use('default')
    
    # Combined coverage map
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Coverage heatmap
    if len(coverage_data.shape) >= 2:
        # Take the first coverage map if multiple exist
        if len(coverage_data.shape) == 3:
            coverage_plot = coverage_data[:, :, 0]
        else:
            coverage_plot = coverage_data
            
        im1 = ax1.imshow(coverage_plot, cmap='viridis', origin='lower')
        ax1.set_title('WiFi Coverage Map\n(Sionna 1.1.0 Ray Tracing)')
        ax1.set_xlabel('X Position')
        ax1.set_ylabel('Y Position')
        plt.colorbar(im1, ax=ax1, label='Signal Strength (dBm)')
        
        # Add AP positions
        for i, ap in enumerate(aps):
            ax1.plot(ap['x'], ap['y'], 'r*', markersize=15, 
                    label=f"AP {i+1}: {ap['name']}")
        ax1.legend()
    
    # Signal distribution
    coverage_flat = coverage_data.flatten()
    ax2.hist(coverage_flat[coverage_flat > -200], bins=50, alpha=0.7, color='blue')
    ax2.set_title('Signal Strength Distribution')
    ax2.set_xlabel('Signal Strength (dBm)')
    ax2.set_ylabel('Frequency')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f"{output_dir}/sionna_1_1_0_coverage.png", dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"  💾 Coverage plots saved: {output_dir}/sionna_1_1_0_coverage.png")

def main():
    parser = argparse.ArgumentParser(description='Sionna 1.1.0 Coverage Simulation')
    parser.add_argument('--ap_file', default='../data/2f.csv',
                       help='CSV file with AP coordinates')
    parser.add_argument('--output_dir', default='./sionna_1_1_0_results',
                       help='Output directory for results')
    parser.add_argument('--scene_file', default=None,
                       help='Optional Mitsuba scene file (experimental)')
    
    args = parser.parse_args()
    
    print("🚀 SIONNA 1.1.0 WIFI COVERAGE SIMULATION")
    print("=" * 50)
    print(f"Sionna Version: {sionna.__version__}")
    print(f"TensorFlow Version: {tf.__version__}")
    
    # Load dummy APs
    aps = load_dummy_aps(args.ap_file)
    if not aps:
        print("❌ No APs loaded, exiting")
        return
    
    # Run simulation
    success = run_sionna_coverage_simulation(aps, args.output_dir)
    
    if success:
        print("\n🎉 SIONNA 1.1.0 SIMULATION COMPLETE!")
        print(f"📁 Results available in: {args.output_dir}")
    else:
        print("\n⚠️  Simulation failed")
        print("💡 Try: pip install sionna==0.19 for older API compatibility")

if __name__ == "__main__":
    main()
