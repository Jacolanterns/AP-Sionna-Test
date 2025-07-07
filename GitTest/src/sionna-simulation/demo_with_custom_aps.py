#!/usr/bin/env python3
"""
Demo script showing how to use custom AP coordinates with Sionna simulation.

This script demonstrates how to:
1. Load custom AP coordinates from CSV files (2f.csv, 3f.csv)
2. Use them with Sionna ray tracing simulation
3. Generate coverage maps for the custom AP layouts

Usage:
    python demo_with_custom_aps.py --ap_file ../data/2f.csv --output_dir ./output_2f
    python demo_with_custom_aps.py --ap_file ../data/3f.csv --output_dir ./output_3f
"""

import os
import sys
import csv
import argparse
import subprocess
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def load_transmitters(filename):
    """
    Load transmitters from a CSV file.
    
    Expected CSV format:
    name,x,y,z
    AP_01,5.0,10.0,3.0
    AP_02,15.0,20.0,3.0
    
    Parameters
    ----------
    filename : str
        Path to CSV file containing AP coordinates
        
    Returns
    -------
    list of tuple
        List of (name, [x, y, z]) tuples
    """
    transmitters = []
    print(f"Loading AP coordinates from: {filename}")
    
    with open(filename, "r") as file:
        csv_reader = csv.reader(file)
        for row_num, row in enumerate(csv_reader, 1):
            if len(row) >= 4:  # name, x, y, z
                name = row[0]
                try:
                    x, y, z = map(float, row[1:4])
                    transmitters.append((name, [x, y, z]))
                    print(f"  {name}: ({x:.1f}, {y:.1f}, {z:.1f})")
                except ValueError as e:
                    print(f"Warning: Could not parse row {row_num}: {row} - {e}")
            else:
                print(f"Warning: Invalid row {row_num}: {row}")
    
    print(f"Loaded {len(transmitters)} AP positions")
    return transmitters

def visualize_ap_layout(transmitters, output_dir, title="AP Layout"):
    """
    Create a 3D visualization of the AP layout.
    
    Parameters
    ----------
    transmitters : list
        List of (name, [x, y, z]) tuples
    output_dir : str
        Directory to save the visualization
    title : str
        Title for the plot
    """
    os.makedirs(output_dir, exist_ok=True)
    
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Extract coordinates
    names = [name for name, pos in transmitters]
    positions = [pos for name, pos in transmitters]
    
    if positions:
        x_coords = [pos[0] for pos in positions]
        y_coords = [pos[1] for pos in positions]
        z_coords = [pos[2] for pos in positions]
        
        # Create scatter plot
        scatter = ax.scatter(x_coords, y_coords, z_coords, 
                           c='red', s=100, alpha=0.8, marker='o')
        
        # Add labels for each AP
        for i, (name, pos) in enumerate(transmitters):
            ax.text(pos[0], pos[1], pos[2], f'  {name}', 
                   fontsize=8, alpha=0.8)
        
        # Set labels and title
        ax.set_xlabel('X (meters)')
        ax.set_ylabel('Y (meters)')
        ax.set_zlabel('Z (meters)')
        ax.set_title(title)
        
        # Add grid
        ax.grid(True, alpha=0.3)
        
        # Save the plot
        output_file = os.path.join(output_dir, "ap_layout_3d.png")
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"AP layout visualization saved to: {output_file}")
        
        # Also create a 2D top-down view
        fig2, ax2 = plt.subplots(figsize=(10, 8))
        ax2.scatter(x_coords, y_coords, c='red', s=100, alpha=0.8, marker='o')
        
        for i, (name, pos) in enumerate(transmitters):
            ax2.annotate(name, (pos[0], pos[1]), xytext=(5, 5), 
                        textcoords='offset points', fontsize=8, alpha=0.8)
        
        ax2.set_xlabel('X (meters)')
        ax2.set_ylabel('Y (meters)')
        ax2.set_title(f"{title} - Top View")
        ax2.grid(True, alpha=0.3)
        ax2.set_aspect('equal', adjustable='box')
        
        output_file_2d = os.path.join(output_dir, "ap_layout_2d.png")
        plt.savefig(output_file_2d, dpi=300, bbox_inches='tight')
        print(f"AP layout 2D view saved to: {output_file_2d}")
        
        plt.close('all')

def simulate_with_sionna(transmitters, mitsuba_file, output_dir):
    """
    Run Sionna simulation with the custom AP coordinates.
    
    This function attempts to run actual Sionna simulation if available,
    otherwise provides detailed instructions for manual execution.
    
    Parameters
    ----------
    transmitters : list
        List of (name, [x, y, z]) tuples
    mitsuba_file : str
        Path to Mitsuba scene file (.xml)
    output_dir : str
        Directory to save simulation results
    """
    print("🚀 Attempting Sionna simulation with:")
    print(f"  📍 Transmitters: {len(transmitters)} APs")
    print(f"  🏗️  Scene file: {mitsuba_file}")
    print(f"  📁 Output directory: {output_dir}")
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Save transmitter coordinates in Sionna format
    transmitter_file = os.path.join(output_dir, "transmitters.csv")
    with open(transmitter_file, 'w') as f:
        for name, pos in transmitters:
            f.write(f"{name},{pos[0]},{pos[1]},{pos[2]}\n")
    print(f"  💾 Saved transmitters to: {transmitter_file}")
    
    # Try to run actual Sionna simulation
    try:
        print("\n🔧 Attempting to run sionna_coverage_map.py...")
        
        # Use the existing sionna_coverage_map.py script
        sionna_script = "./sionna_coverage_map.py"
        if os.path.exists(sionna_script):
            import subprocess
            cmd = [
                "python", sionna_script,
                "--transmitter_file", transmitter_file,
                "--mitsuba_file", mitsuba_file,
                "--output_dir", output_dir
            ]
            
            print(f"🎯 Running: {' '.join(cmd)}")
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            
            if result.returncode == 0:
                print("✅ Sionna simulation completed successfully!")
                print("📊 Output:")
                print(result.stdout)
                return True
            else:
                print("❌ Sionna simulation failed:")
                print(result.stderr)
                return False
        else:
            print(f"❌ Sionna script not found: {sionna_script}")
            return False
            
    except subprocess.TimeoutExpired:
        print("⏰ Simulation timed out (5 minutes limit)")
        return False
    except Exception as e:
        print(f"❌ Error running simulation: {e}")
        return False

def find_available_scene_files():
    """
    Find available Mitsuba scene files in the project.
    
    Returns
    -------
    list
        List of available scene file paths
    """
    scene_files = []
    
    # Check common locations for scene files
    search_paths = [
        "./simple_scene.xml",
        "/home/sionna/Documents/GitHub/wifi-cco/sionna-simulation/simple_scene.xml",
        "/home/sionna/Documents/GitHub/nvidia-sionna/docs/Blender/Floorplan/2F_No_AP.xml",
        "/home/sionna/Documents/GitHub/nvidia-sionna/docs/Blender/try_scene/untitled.xml"
    ]
    
    for path in search_paths:
        if os.path.exists(path):
            scene_files.append(path)
    
    return scene_files

def main():
    parser = argparse.ArgumentParser(description="Demo: Use custom AP coordinates with Sionna")
    parser.add_argument('--ap_file', type=str, required=True, 
                       help='CSV file with AP coordinates (name,x,y,z)')
    parser.add_argument('--output_dir', type=str, default='./output', 
                       help='Directory to save results')
    parser.add_argument('--mitsuba_file', type=str, 
                       help='Mitsuba scene file (optional, will auto-detect if not provided)')
    parser.add_argument('--run_simulation', action='store_true',
                       help='Attempt to run actual Sionna simulation')
    
    args = parser.parse_args()
    
    # Validate input file
    if not os.path.exists(args.ap_file):
        print(f"Error: AP file not found: {args.ap_file}")
        return 1
    
    print("=" * 70)
    print("🎯 CUSTOM AP COORDINATES → SIONNA SIMULATION DEMO")
    print("=" * 70)
    
    # Load AP coordinates
    try:
        transmitters = load_transmitters(args.ap_file)
        if not transmitters:
            print("Error: No valid AP coordinates found in file")
            return 1
    except Exception as e:
        print(f"Error loading AP coordinates: {e}")
        return 1
    
    # Create output directory
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Visualize AP layout
    floor_name = Path(args.ap_file).stem.upper()  # e.g., "2F" from "2f.csv"
    print(f"\n📊 Creating visualizations for Floor {floor_name}...")
    visualize_ap_layout(transmitters, args.output_dir, 
                       title=f"Floor {floor_name} AP Layout")
    
    # Generate summary report
    report_file = os.path.join(args.output_dir, "ap_summary.txt")
    with open(report_file, 'w') as f:
        f.write(f"AP Coordinate Summary for {floor_name}\n")
        f.write("=" * 40 + "\n\n")
        f.write(f"Source file: {args.ap_file}\n")
        f.write(f"Number of APs: {len(transmitters)}\n\n")
        f.write("AP Coordinates:\n")
        for name, pos in transmitters:
            f.write(f"  {name}: ({pos[0]:.1f}, {pos[1]:.1f}, {pos[2]:.1f})\n")
        
        if transmitters:
            positions = [pos for name, pos in transmitters]
            x_coords = [pos[0] for pos in positions]
            y_coords = [pos[1] for pos in positions]
            z_coords = [pos[2] for pos in positions]
            
            f.write(f"\nBounding Box:\n")
            f.write(f"  X: {min(x_coords):.1f} to {max(x_coords):.1f}\n")
            f.write(f"  Y: {min(y_coords):.1f} to {max(y_coords):.1f}\n")
            f.write(f"  Z: {min(z_coords):.1f} to {max(z_coords):.1f}\n")
        
        f.write(f"\nTo use with Sionna simulation:\n")
        f.write(f"python sionna_coverage_map.py \\\n")
        f.write(f"  --transmitter_file {args.ap_file} \\\n")
        f.write(f"  --mitsuba_file path/to/scene.xml \\\n")
        f.write(f"  --output_dir {args.output_dir}/sionna_results\n")
    
    print(f"📄 Summary report saved to: {report_file}")
    
    # Find available scene files
    print(f"\n🔍 Searching for available building scene files...")
    available_scenes = find_available_scene_files()
    
    if available_scenes:
        print(f"✅ Found {len(available_scenes)} scene file(s):")
        for i, scene in enumerate(available_scenes, 1):
            print(f"  {i}. {scene}")
        
        # Use provided scene file or the first available one
        if args.mitsuba_file:
            if os.path.exists(args.mitsuba_file):
                scene_file = args.mitsuba_file
                print(f"🎯 Using provided scene file: {scene_file}")
            else:
                print(f"❌ Provided scene file not found: {args.mitsuba_file}")
                scene_file = available_scenes[0]
                print(f"🎯 Falling back to: {scene_file}")
        else:
            scene_file = available_scenes[0]
            print(f"🎯 Auto-selected scene file: {scene_file}")
        
        # Run simulation if requested
        if args.run_simulation:
            print(f"\n🚀 Running Sionna simulation...")
            success = simulate_with_sionna(transmitters, scene_file, 
                                         os.path.join(args.output_dir, "sionna_results"))
            if success:
                print(f"✅ Simulation completed successfully!")
            else:
                print(f"❌ Simulation failed - see output above for details")
        else:
            print(f"\n💡 To run actual Sionna simulation, use --run_simulation flag")
            print(f"   Example: python {sys.argv[0]} --ap_file {args.ap_file} --run_simulation")
            
    else:
        print(f"❌ No scene files found in common locations")
        print(f"💡 Available Blender files found:")
        blender_files = [
            "/home/sionna/Documents/GitHub/wifi-cco/sionna-simulation/data/blender/2F_no_solid.blend",
            "/home/sionna/Documents/GitHub/nvidia-sionna/docs/Blender/Floorplan/2F_No_AP.blend"
        ]
        for bf in blender_files:
            if os.path.exists(bf):
                print(f"   📁 {bf}")
        print(f"   Convert these to Mitsuba .xml format for simulation")
    
    print(f"\n" + "=" * 70)
    print(f"✅ Demo completed! Results saved to: {args.output_dir}")
    print(f"🎯 Your AP coordinates are ready for Sionna simulation.")
    
    return 0

if __name__ == "__main__":
    exit(main())
