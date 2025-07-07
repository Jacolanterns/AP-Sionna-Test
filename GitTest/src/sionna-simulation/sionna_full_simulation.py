#!/usr/bin/env python3
"""
Full Sionna Ray Tracing Simulation with Dummy APs and 2F Building
=================================================================

This script runs the complete Sionna workflow:
1. Load Blender scene (2F_no_solid.blend)
2. Add random obstacles (optional)
3. Convert to Mitsuba format
4. Run Sionna ray tracing simulation
5. Generate coverage maps
6. Add coverage visualizations to 3D scene
7. Export to various formats (USD, GLB)

Usage:
    python sionna_full_simulation.py --num_cubes 5 --coverage_type combined
"""

import argparse
import subprocess
import os
import csv
import sys
import xml.etree.ElementTree as ET

# Define root and file paths for current setup
ROOT = "/home/sionna/Documents/GitTest/src/sionna-simulation"

# Input files
BLEND_FILE_PATH = "/home/sionna/Documents/GitHub/wifi-cco/sionna-simulation/data/blender/2F_no_solid.blend"
TRANSMITTER_FILE = os.path.join(ROOT, "../data/2f.csv")  # Use our dummy AP data

# Output files
OUTPUT_BLEND_PATH = os.path.join(ROOT, "output_scene.blend")
OUTPUT_MITSUBA_PATH = os.path.join(ROOT, "output_scene.xml")
OUTPUT_BLEND_PATH_3D = os.path.join(ROOT, "output_scene_with_3d_mesh.blend")
OUTPUT_USD_PATH_3D = os.path.join(ROOT, "output_scene_with_3d_mesh.usdc")
OUTPUT_GLB_PATH_3D = os.path.join(ROOT, "output_scene_with_3d_mesh.glb")

# Blender scripts directory
SCRIPTS_DIR = ROOT

def setup_parser():
    """Setup command line argument parser."""
    parser = argparse.ArgumentParser(description="Run full Sionna ray tracing simulation.")
    parser.add_argument('--num_cubes', type=int, default=5, 
                       help='Number of random cubes to add as obstacles (default: 5)')
    parser.add_argument('--coverage_type', choices=['individual', 'combined'], default='combined',
                       help='Type of coverage map to display (default: combined)')
    parser.add_argument('--skip_cubes', action='store_true',
                       help='Skip adding random cubes (use clean scene)')
    parser.add_argument('--transmitter_file', type=str, default=TRANSMITTER_FILE,
                       help='CSV file with transmitter locations')
    return parser

def check_dependencies():
    """Check if required dependencies are available."""
    print("🔍 Checking dependencies...")
    
    # Check if Blender is available
    try:
        result = subprocess.run(['blender', '--version'], capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print("✅ Blender found")
        else:
            print("❌ Blender not found. Please install Blender.")
            return False
    except (subprocess.TimeoutExpired, FileNotFoundError):
        print("❌ Blender not found. Please install Blender.")
        return False
    
    # Check if input files exist
    if not os.path.exists(BLEND_FILE_PATH):
        print(f"❌ Blender file not found: {BLEND_FILE_PATH}")
        return False
    else:
        print(f"✅ Blender scene found: {BLEND_FILE_PATH}")
    
    if not os.path.exists(TRANSMITTER_FILE):
        print(f"❌ Transmitter file not found: {TRANSMITTER_FILE}")
        return False
    else:
        print(f"✅ Transmitter data found: {TRANSMITTER_FILE}")
    
    # Check if required scripts exist
    required_scripts = [
        'blender_add_cubes.py',
        'save_to_mitsuba.py', 
        'sionna_coverage_map.py',
        'blender_add_single_coverage_map.py',
        'blender_add_3d_heatmap.py'
    ]
    
    for script in required_scripts:
        script_path = os.path.join(SCRIPTS_DIR, script)
        if not os.path.exists(script_path):
            print(f"❌ Required script not found: {script_path}")
            return False
    
    print("✅ All required scripts found")
    return True

def correct_orientation(file_path):
    """
    Correct the orientation of objects in the Mitsuba XML file.
    
    This ensures proper object positioning for Sionna ray tracing.
    """
    print(f"🔧 Correcting orientation in {file_path}")
    
    tree = ET.parse(file_path)
    root = tree.getroot()

    rotates = [
        {"axis": "x", "angle": "90"},
        {"axis": "y", "angle": "0"},
        {"axis": "z", "angle": "-90"},
    ]

    for shape in root.findall(".//shape"):
        # Rename the shape
        filename_element = shape.find("./string[@name='filename']")
        if filename_element is not None:
            filename = filename_element.attrib['value']
            base_name = os.path.splitext(os.path.basename(filename))[0]
            shape.set('id', f"{base_name}")
            shape.set('name', f"{base_name}")

        # Remove existing transform if present
        existing_transform = shape.find('transform')
        if existing_transform is not None:
            shape.remove(existing_transform)

        # Create new transform
        transform = ET.Element('transform')
        transform.set('name', 'to_world')

        # Add rotate elements
        for rotate_info in rotates:
            rotate = ET.Element('rotate')
            rotate.set(rotate_info['axis'], "1")
            rotate.set('angle', rotate_info['angle'])
            transform.append(rotate)

        # Add translate element
        translate = ET.Element('translate')
        translate.set('value', "0 0 0")
        transform.append(translate)

        # Insert the new transform as the first child of the shape
        shape.insert(0, transform)

    tree.write(file_path, encoding='utf-8', xml_declaration=True)

def run_blender_script(script_path, arguments, description=""):
    """
    Run a Blender script with specified arguments.
    """
    if description:
        print(f"🎨 {description}")
    
    cmd = [
        "blender",
        "--background",
        "--python", script_path,
        "--"
    ] + arguments
    
    print(f"   Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, check=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ Error running Blender script: {script_path}")
        print(f"Error output: {result.stderr}")
        return False
    return True

def count_transmitters(transmitter_file):
    """Count the number of transmitters in the CSV file."""
    try:
        with open(transmitter_file, 'r') as f:
            reader = csv.reader(f)
            next(reader, None)  # Skip header if present
            return sum(1 for _ in reader)
    except Exception as e:
        print(f"❌ Error reading transmitter file: {e}")
        return 0

def main():
    parser = setup_parser()
    args = parser.parse_args()
    
    print("🚀 SIONNA FULL RAY TRACING SIMULATION")
    print("=====================================")
    print(f"📡 Transmitter file: {args.transmitter_file}")
    print(f"🏗️  Building scene: {BLEND_FILE_PATH}")
    print(f"🎯 Coverage type: {args.coverage_type}")
    print(f"📦 Random cubes: {args.num_cubes if not args.skip_cubes else 'None'}")
    print()
    
    # Check dependencies
    if not check_dependencies():
        print("❌ Dependency check failed. Please resolve issues and try again.")
        sys.exit(1)
    
    print("\n🎯 Starting simulation workflow...")
    
    try:
        # Step 1: Add random cubes (obstacles) to the scene
        if not args.skip_cubes:
            print(f"\n📦 Step 1: Adding {args.num_cubes} random cubes to the scene...")
            success = run_blender_script(
                os.path.join(SCRIPTS_DIR, "blender_add_cubes.py"),
                [
                    "--num_cubes", str(args.num_cubes),
                    "--input_blend", BLEND_FILE_PATH,
                    "--output_blend", OUTPUT_BLEND_PATH,
                ],
                f"Adding {args.num_cubes} random obstacles"
            )
            if not success:
                print("❌ Failed to add cubes to scene")
                sys.exit(1)
        else:
            print("\n📦 Step 1: Using clean scene (no additional cubes)")
            # Just copy the original file
            import shutil
            shutil.copy2(BLEND_FILE_PATH, OUTPUT_BLEND_PATH)
        
        # Step 2: Convert Blender scene to Mitsuba format
        print("\n🔄 Step 2: Converting scene to Mitsuba format...")
        cmd = [
            "blender",
            "--background",
            OUTPUT_BLEND_PATH,
            "--python", os.path.join(SCRIPTS_DIR, "save_to_mitsuba.py"),
            "--",
            "--input_blend", OUTPUT_BLEND_PATH,
            "--output_mitsuba", OUTPUT_MITSUBA_PATH
        ]
        
        result = subprocess.run(cmd, check=False, capture_output=True, text=True)
        if not os.path.exists(OUTPUT_MITSUBA_PATH):
            print("❌ Failed to generate Mitsuba file")
            print(f"Error: {result.stderr}")
            sys.exit(1)
        
        # Correct orientation
        correct_orientation(OUTPUT_MITSUBA_PATH)
        print("✅ Mitsuba scene generated successfully")
        
        # Step 3: Run Sionna ray tracing simulation
        print("\n📡 Step 3: Running Sionna ray tracing simulation...")
        print("   This may take several minutes depending on scene complexity...")
        
        result = subprocess.run([
            "python", os.path.join(SCRIPTS_DIR, "sionna_coverage_map.py"),
            "--mitsuba_file", OUTPUT_MITSUBA_PATH,
            "--transmitter_file", args.transmitter_file,
            "--output_dir", ROOT
        ], check=True, capture_output=True, text=True)
        
        print("✅ Sionna simulation completed successfully")
        
        # Count transmitters for visualization
        num_transmitters = count_transmitters(args.transmitter_file)
        print(f"📊 Found {num_transmitters} transmitters")
        
        # Step 4: Add coverage maps to the 3D scene
        print(f"\n🎨 Step 4: Adding {args.coverage_type} coverage maps to the scene...")
        
        if args.coverage_type == 'individual' and num_transmitters > 1:
            success = run_blender_script(
                os.path.join(SCRIPTS_DIR, "blender_add_heatmaps.py"),
                [
                    "--num_planes", str(num_transmitters), 
                    "--input_blend", OUTPUT_BLEND_PATH,
                    "--output_blend", OUTPUT_BLEND_PATH
                ],
                "Adding individual coverage maps"
            )
        else:
            success = run_blender_script(
                os.path.join(SCRIPTS_DIR, "blender_add_single_coverage_map.py"),
                [
                    "--input_blend", OUTPUT_BLEND_PATH,
                    "--output_blend", OUTPUT_BLEND_PATH,
                    "--image_path", os.path.join(ROOT, "sionna_coverage_full_map.png")
                ],
                "Adding combined coverage map"
            )
        
        if not success:
            print("❌ Failed to add coverage maps to scene")
            sys.exit(1)
        
        # Step 5: Create 3D mesh representation
        print("\n🎯 Step 5: Creating 3D mesh from coverage data...")
        mesh_success = run_blender_script(
            os.path.join(SCRIPTS_DIR, "blender_add_3d_heatmap.py"),
            [
                "--input_blend", OUTPUT_BLEND_PATH,
                "--output_file", OUTPUT_BLEND_PATH_3D,
                "--image_path", os.path.join(ROOT, "sionna_coverage_full_map.png")
            ],
            "Creating 3D coverage mesh"
        )
        
        if not mesh_success:
            print("⚠️  Warning: Failed to create 3D mesh, continuing without it")
        
        print("\n✅ SIMULATION COMPLETED SUCCESSFULLY!")
        print("=====================================")
        print("📁 Generated files:")
        print(f"   🎨 Blender scene: {OUTPUT_BLEND_PATH}")
        if os.path.exists(OUTPUT_BLEND_PATH_3D):
            print(f"   🎯 3D mesh scene: {OUTPUT_BLEND_PATH_3D}")
        print(f"   🏗️  Mitsuba scene: {OUTPUT_MITSUBA_PATH}")
        
        # Check for generated coverage maps
        coverage_files = [f for f in os.listdir(ROOT) if f.startswith('sionna_coverage_') and f.endswith('.png')]
        if coverage_files:
            print("   🖼️  Coverage maps:")
            for f in sorted(coverage_files):
                print(f"      - {f}")
        
        print("\n🎉 Full Sionna ray tracing simulation with dummy APs completed!")
        print("🎯 Your wireless coverage analysis is ready for review.")
        
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Simulation failed with error: {e}")
        print(f"Command: {' '.join(e.cmd)}")
        if e.stderr:
            print(f"Error output: {e.stderr}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n⚠️  Simulation interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
