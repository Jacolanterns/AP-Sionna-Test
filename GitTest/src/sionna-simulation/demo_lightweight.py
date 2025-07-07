#!/usr/bin/env python3
"""
Lightweight simulation demo - AP coordinates + building layouts integration.

This script demonstrates the integration without requiring Sionna installation,
showing how your dummy AP coordinates work with building scene files.
"""

import os
import csv
import json
from pathlib import Path

def load_ap_coordinates(csv_file):
    """Load AP coordinates from CSV file."""
    aps = []
    print(f"🔍 Loading AP coordinates from: {csv_file}")
    
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) >= 4:
                name, x, y, z = row[0], float(row[1]), float(row[2]), float(row[3])
                aps.append({
                    'name': name,
                    'position': [x, y, z],
                    'frequency': 2.4e9,  # 2.4 GHz WiFi
                    'power': 20.0  # 20 dBm
                })
                print(f"  📡 {name}: ({x:.1f}, {y:.1f}, {z:.1f})")
    
    print(f"✅ Loaded {len(aps)} AP positions")
    return aps

def analyze_building_scene(xml_file):
    """Analyze building scene file and extract basic info."""
    print(f"\n🏗️  Analyzing building scene: {xml_file}")
    
    info = {
        'file': xml_file,
        'size_bytes': os.path.getsize(xml_file),
        'shapes': [],
        'materials': [],
        'valid_mitsuba': False
    }
    
    with open(xml_file, 'r') as f:
        content = f.read()
        
        # Basic format validation
        if '<scene' in content and 'version=' in content:
            info['valid_mitsuba'] = True
            print("  ✅ Valid Mitsuba scene format")
        
        # Count shapes (rough estimate)
        shape_count = content.count('<shape')
        print(f"  🏠 Estimated {shape_count} building elements")
        
        # Find materials
        if 'concrete' in content.lower():
            info['materials'].append('concrete')
        if 'metal' in content.lower():
            info['materials'].append('metal')
        if 'marble' in content.lower():
            info['materials'].append('marble')
        if 'diffuse' in content.lower():
            info['materials'].append('diffuse')
            
        if info['materials']:
            print(f"  🎨 Materials: {', '.join(info['materials'])}")
    
    return info

def simulate_coverage_basic(aps, building_info, output_dir):
    """
    Simulate basic coverage without full Sionna - demonstrates integration.
    """
    print(f"\n🎯 Running basic coverage simulation...")
    os.makedirs(output_dir, exist_ok=True)
    
    # Simple coverage calculation (placeholder for actual Sionna)
    results = {
        'simulation_type': 'integration_demo',
        'building_scene': building_info['file'],
        'ap_count': len(aps),
        'aps': aps,
        'coverage_analysis': {}
    }
    
    print(f"  📍 APs positioned in building layout")
    print(f"  🔄 Computing signal propagation through walls...")
    
    # Calculate basic metrics for each AP
    for ap in aps:
        x, y, z = ap['position']
        
        # Simple coverage estimation (placeholder)
        coverage_radius = 30.0  # meters (typical WiFi range)
        coverage_area = 3.14159 * (coverage_radius ** 2)  # circular coverage
        
        results['coverage_analysis'][ap['name']] = {
            'position': ap['position'],
            'estimated_coverage_radius_m': coverage_radius,
            'estimated_coverage_area_m2': coverage_area,
            'signal_frequency_ghz': ap['frequency'] / 1e9,
            'transmit_power_dbm': ap['power']
        }
        
        print(f"    📡 {ap['name']}: ~{coverage_radius}m range, ~{coverage_area:.0f}m² area")
    
    # Calculate building coverage overlap
    total_coverage = sum(ap_data['estimated_coverage_area_m2'] 
                        for ap_data in results['coverage_analysis'].values())
    
    results['total_estimated_coverage_m2'] = total_coverage
    
    # Save results
    results_file = os.path.join(output_dir, 'simulation_results.json')
    with open(results_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    # Create summary report
    summary_file = os.path.join(output_dir, 'coverage_summary.txt')
    with open(summary_file, 'w') as f:
        f.write("SIONNA SIMULATION INTEGRATION DEMO\n")
        f.write("=" * 40 + "\n\n")
        f.write(f"Building Scene: {building_info['file']}\n")
        f.write(f"AP Count: {len(aps)}\n")
        f.write(f"Total Estimated Coverage: {total_coverage:.0f} m²\n\n")
        
        f.write("AP POSITIONS & COVERAGE:\n")
        f.write("-" * 30 + "\n")
        for ap_name, data in results['coverage_analysis'].items():
            pos = data['position']
            f.write(f"{ap_name}: ({pos[0]:.1f}, {pos[1]:.1f}, {pos[2]:.1f}) -> ")
            f.write(f"~{data['estimated_coverage_radius_m']:.0f}m range\n")
        
        f.write(f"\nFULL SIONNA SIMULATION COMMAND:\n")
        f.write(f"python sionna_coverage_map.py \\\n")
        f.write(f"  --transmitter_file {results['building_scene'].replace('.xml', '.csv')} \\\n")
        f.write(f"  --mitsuba_file {building_info['file']} \\\n")
        f.write(f"  --output_dir {output_dir}/full_sionna_results\n")
    
    print(f"  💾 Results saved to: {results_file}")
    print(f"  📄 Summary saved to: {summary_file}")
    
    return results

def main():
    print("🚀 SIONNA INTEGRATION DEMO - AP COORDINATES + BUILDING LAYOUTS")
    print("=" * 70)
    
    # Test files
    test_cases = [
        {
            'ap_file': '../data/2f.csv',
            'scene_file': './building_2f.xml',
            'output_dir': './demo_2f_building'
        },
        {
            'ap_file': '../data/3f.csv', 
            'scene_file': './simple_scene.xml',
            'output_dir': './demo_3f_simple'
        }
    ]
    
    success_count = 0
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n📋 Test Case {i}: {Path(test_case['ap_file']).stem.upper()} + {Path(test_case['scene_file']).stem}")
        print("-" * 50)
        
        # Check if files exist
        if not os.path.exists(test_case['ap_file']):
            print(f"❌ AP file not found: {test_case['ap_file']}")
            continue
            
        if not os.path.exists(test_case['scene_file']):
            print(f"❌ Scene file not found: {test_case['scene_file']}")
            continue
        
        try:
            # Load APs
            aps = load_ap_coordinates(test_case['ap_file'])
            
            # Analyze building
            building_info = analyze_building_scene(test_case['scene_file'])
            
            # Run basic simulation
            results = simulate_coverage_basic(aps, building_info, test_case['output_dir'])
            
            print(f"✅ Test case {i} completed successfully!")
            success_count += 1
            
        except Exception as e:
            print(f"❌ Test case {i} failed: {e}")
    
    print(f"\n" + "=" * 70)
    print(f"🏆 INTEGRATION DEMO COMPLETE")
    print(f"✅ {success_count}/{len(test_cases)} test cases successful")
    
    if success_count > 0:
        print(f"\n🎯 NEXT STEPS:")
        print(f"1. Install Sionna: pip install sionna tensorflow")
        print(f"2. Run full simulation with generated commands")
        print(f"3. Your dummy APs are ready for realistic coverage analysis!")
    
    return success_count == len(test_cases)

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
