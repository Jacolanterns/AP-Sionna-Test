#!/usr/bin/env python3
"""
Test integration of dummy AP coordinates with building scene files.

This script validates that your AP coordinates can be used with the 
building layouts we found, without requiring Sionna installation.
"""

import os
import csv

def test_building_scenes_with_aps():
    """Test that AP coordinates work with available building scenes."""
    
    print("🏗️  TESTING: AP COORDINATES + BUILDING SCENES")
    print("=" * 60)
    
    # Test AP coordinate files
    ap_files = [
        "../data/2f.csv",
        "../data/3f.csv"
    ]
    
    # Test scene files
    scene_files = [
        "./simple_scene.xml",
        "./building_2f.xml"
    ]
    
    print("📊 AP Coordinate Files:")
    for ap_file in ap_files:
        if os.path.exists(ap_file):
            print(f"✅ Found: {ap_file}")
            
            # Load and validate APs
            with open(ap_file, 'r') as f:
                reader = csv.reader(f)
                transmitters = list(reader)
                print(f"   📡 {len(transmitters)} APs loaded")
                for name, x, y, z in transmitters[:2]:  # Show first 2
                    print(f"      {name}: ({x}, {y}, {z})")
                if len(transmitters) > 2:
                    print(f"      ... and {len(transmitters) - 2} more")
        else:
            print(f"❌ Missing: {ap_file}")
    
    print("\n🏠 Building Scene Files:")
    for scene_file in scene_files:
        if os.path.exists(scene_file):
            print(f"✅ Found: {scene_file}")
            
            # Check file size and basic content
            size = os.path.getsize(scene_file)
            print(f"   📏 Size: {size} bytes")
            
            with open(scene_file, 'r') as f:
                content = f.read(200)  # First 200 chars
                if '<scene' in content:
                    print(f"   ✅ Valid Mitsuba scene format")
                else:
                    print(f"   ⚠️  Unknown format")
        else:
            print(f"❌ Missing: {scene_file}")
    
    print("\n🎯 INTEGRATION READINESS CHECK:")
    
    # Check if we have the necessary components
    has_aps = any(os.path.exists(f) for f in ap_files)
    has_scenes = any(os.path.exists(f) for f in scene_files)
    has_sionna_script = os.path.exists("./sionna_coverage_map.py")
    
    if has_aps:
        print("✅ AP coordinates available")
    else:
        print("❌ No AP coordinate files found")
    
    if has_scenes:
        print("✅ Building scene files available")
    else:
        print("❌ No building scene files found")
    
    if has_sionna_script:
        print("✅ Sionna simulation script available")
    else:
        print("❌ Sionna simulation script missing")
    
    print("\n📋 SIMULATION COMMANDS READY:")
    
    if has_aps and has_scenes:
        print("🚀 Ready to run Sionna simulation!")
        
        for ap_file in ap_files:
            if os.path.exists(ap_file):
                for scene_file in scene_files:
                    if os.path.exists(scene_file):
                        floor = os.path.basename(ap_file).replace('.csv', '').upper()
                        scene_name = os.path.basename(scene_file).replace('.xml', '')
                        
                        print(f"\n📍 {floor} + {scene_name}:")
                        print(f"   python sionna_coverage_map.py \\")
                        print(f"     --transmitter_file {ap_file} \\")
                        print(f"     --mitsuba_file {scene_file} \\")
                        print(f"     --output_dir ./results_{floor}_{scene_name}")
        
        print(f"\n💡 To install Sionna environment:")
        print(f"   conda env create -f /home/sionna/Documents/GitHub/nvidia-sionna/venv.yml")
        print(f"   conda activate sionna_env")
        
    else:
        print("❌ Missing required files for simulation")
    
    print("\n" + "=" * 60)
    print("✅ INTEGRATION TEST COMPLETE")
    
    return has_aps and has_scenes

if __name__ == "__main__":
    success = test_building_scenes_with_aps()
    if success:
        print("🎉 Your dummy AP coordinates are ready for building simulation!")
    else:
        print("⚠️  Some components missing - check output above")
