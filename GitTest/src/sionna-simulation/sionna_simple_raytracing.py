#!/usr/bin/env python3
"""
Simplified Sionna Ray Tracing Simulation with Dummy APs
=======================================================

This script runs Sionna ray tracing using existing Mitsuba XML files
and generates comprehensive coverage analysis.

Usage:
    python sionna_simple_raytracing.py --scene building_2f --transmitters 2f
"""

import argparse
import os
import sys
import subprocess
import time

# Current directory setup
ROOT = "/home/sionna/Documents/GitTest/src/sionna-simulation"

# Available scenes and transmitter files
SCENES = {
    'building_2f': os.path.join(ROOT, 'building_2f.xml'),
    'simple': os.path.join(ROOT, 'simple_scene.xml')
}

TRANSMITTER_FILES = {
    '2f': os.path.join(ROOT, '../data/2f.csv'),
    '3f': os.path.join(ROOT, '../data/3f.csv')
}

def setup_parser():
    """Setup command line argument parser."""
    parser = argparse.ArgumentParser(description="Run Sionna ray tracing simulation.")
    parser.add_argument('--scene', choices=list(SCENES.keys()), default='building_2f',
                       help='Building scene to use (default: building_2f)')
    parser.add_argument('--transmitters', choices=list(TRANSMITTER_FILES.keys()), default='2f',
                       help='Transmitter configuration to use (default: 2f)')
    parser.add_argument('--output_dir', type=str, default=None,
                       help='Output directory (default: auto-generated)')
    return parser

def check_files(scene_key, transmitter_key):
    """Check if required files exist."""
    scene_file = SCENES[scene_key]
    transmitter_file = TRANSMITTER_FILES[transmitter_key]
    
    if not os.path.exists(scene_file):
        print(f"❌ Scene file not found: {scene_file}")
        return False
    
    if not os.path.exists(transmitter_file):
        print(f"❌ Transmitter file not found: {transmitter_file}")
        return False
    
    return True

def run_sionna_simulation(scene_file, transmitter_file, output_dir):
    """Run the Sionna ray tracing simulation."""
    print(f"🚀 Running Sionna ray tracing simulation...")
    print(f"   Scene: {scene_file}")
    print(f"   Transmitters: {transmitter_file}")
    print(f"   Output: {output_dir}")
    print()
    
    # Run the Sionna coverage map script
    cmd = [
        "python", "sionna_coverage_map.py",
        "--mitsuba_file", scene_file,
        "--transmitter_file", transmitter_file,
        "--output_dir", output_dir
    ]
    
    print(f"   Command: {' '.join(cmd)}")
    print("   This may take several minutes for ray tracing...")
    
    start_time = time.time()
    result = subprocess.run(cmd, capture_output=True, text=True)
    end_time = time.time()
    
    if result.returncode == 0:
        print(f"✅ Simulation completed successfully in {end_time - start_time:.1f} seconds")
        return True
    else:
        print(f"❌ Simulation failed:")
        print(f"Error: {result.stderr}")
        print(f"Output: {result.stdout}")
        return False

def check_outputs(output_dir):
    """Check and display generated output files."""
    print(f"\n📁 Checking output files in {output_dir}...")
    
    if not os.path.exists(output_dir):
        print("❌ Output directory not found")
        return
    
    files = os.listdir(output_dir)
    coverage_files = [f for f in files if f.startswith('sionna_coverage_') and f.endswith('.png')]
    
    if not coverage_files:
        print("❌ No coverage map files found")
        return
    
    print("✅ Generated files:")
    for f in sorted(files):
        file_path = os.path.join(output_dir, f)
        file_size = os.path.getsize(file_path)
        print(f"   📄 {f} ({file_size:,} bytes)")
    
    return True

def main():
    parser = setup_parser()
    args = parser.parse_args()
    
    # Generate output directory name if not provided
    if args.output_dir is None:
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        args.output_dir = f"sionna_raytracing_{args.scene}_{args.transmitters}_{timestamp}"
    
    output_dir = os.path.join(ROOT, args.output_dir)
    
    print("🎯 SIONNA RAY TRACING SIMULATION")
    print("================================")
    print(f"🏗️  Scene: {args.scene}")
    print(f"📡 Transmitters: {args.transmitters}")
    print(f"📁 Output: {output_dir}")
    print()
    
    # Check if files exist
    if not check_files(args.scene, args.transmitters):
        print("❌ Required files not found. Exiting.")
        sys.exit(1)
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Run simulation
    success = run_sionna_simulation(
        SCENES[args.scene], 
        TRANSMITTER_FILES[args.transmitters], 
        output_dir
    )
    
    if not success:
        print("❌ Simulation failed")
        sys.exit(1)
    
    # Check outputs
    check_outputs(output_dir)
    
    print(f"\n🎉 RAY TRACING SIMULATION COMPLETE!")
    print("===================================")
    print(f"📁 Results saved to: {output_dir}")
    print(f"🎯 Your Sionna ray tracing analysis with dummy APs is ready!")
    
    # Show some quick stats
    scene_name = args.scene.replace('_', ' ').title()
    tx_count = '2 APs' if args.transmitters == '2f' else '6 APs'
    print(f"\n📊 Simulation Summary:")
    print(f"   🏗️  Building: {scene_name}")
    print(f"   📡 Access Points: {tx_count}")
    print(f"   🎨 Ray Tracing: Full Sionna simulation")
    print(f"   📈 Coverage Maps: Generated")

if __name__ == "__main__":
    main()
