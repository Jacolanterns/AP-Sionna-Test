#!/usr/bin/env python3
"""
Complete pipeline integration: AP prediction → Sionna simulation

This script bridges your AP prediction pipeline with Sionna ray tracing simulation:
1. Uses AP coordinates from your ML pipeline (real or dummy)
2. Prepares them for Sionna simulation
3. Provides ready-to-run simulation commands
4. Demonstrates the complete workflow

Usage:
    python ap_to_sionna_pipeline.py --mode validate --ap_file ../data/2f.csv
    python ap_to_sionna_pipeline.py --mode simulate --ap_file ../data/2f.csv --scene scene.xml
    python ap_to_sionna_pipeline.py --mode pipeline --building D1 --date 2024-07-01
"""

import os
import sys
import csv
import argparse
import subprocess
from pathlib import Path
from datetime import datetime

def validate_ap_coordinates(ap_file):
    """
    Validate AP coordinate file format for Sionna compatibility.
    
    Returns
    -------
    tuple
        (is_valid, transmitters, errors)
    """
    errors = []
    transmitters = []
    
    if not os.path.exists(ap_file):
        return False, [], [f"File not found: {ap_file}"]
    
    try:
        with open(ap_file, 'r') as f:
            csv_reader = csv.reader(f)
            for row_num, row in enumerate(csv_reader, 1):
                if len(row) < 4:
                    errors.append(f"Row {row_num}: Insufficient columns (need name,x,y,z)")
                    continue
                
                name = row[0].strip()
                if not name:
                    errors.append(f"Row {row_num}: Empty AP name")
                    continue
                
                try:
                    x, y, z = map(float, row[1:4])
                    transmitters.append((name, [x, y, z]))
                except ValueError as e:
                    errors.append(f"Row {row_num}: Invalid coordinates - {e}")
        
        if not transmitters:
            errors.append("No valid AP coordinates found")
        
        return len(errors) == 0, transmitters, errors
        
    except Exception as e:
        return False, [], [f"Error reading file: {e}"]

def prepare_sionna_simulation(transmitters, output_dir, scene_file=None):
    """
    Prepare files and commands for Sionna simulation.
    
    Parameters
    ----------
    transmitters : list
        List of (name, [x, y, z]) tuples
    output_dir : str
        Directory for simulation outputs
    scene_file : str, optional
        Path to Mitsuba scene file
    
    Returns
    -------
    dict
        Simulation configuration and commands
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # Create transmitter file in Sionna format
    sionna_transmitter_file = os.path.join(output_dir, "transmitters.csv")
    with open(sionna_transmitter_file, 'w') as f:
        for name, pos in transmitters:
            f.write(f"{name},{pos[0]},{pos[1]},{pos[2]}\n")
    
    # Prepare simulation commands
    commands = {}
    
    if scene_file and os.path.exists(scene_file):
        # Full simulation with scene
        commands['full_simulation'] = [
            "python", "sionna_coverage_map.py",
            "--transmitter_file", sionna_transmitter_file,
            "--mitsuba_file", scene_file,
            "--output_dir", os.path.join(output_dir, "coverage_results")
        ]
    
    # Validation command (always available)
    commands['validate'] = [
        "python", "-c", 
        f"import csv; "
        f"print('Validating {sionna_transmitter_file}'); "
        f"with open('{sionna_transmitter_file}', 'r') as f: "
        f"    transmitters = list(csv.reader(f)); "
        f"print(f'Found {{len(transmitters)}} transmitters'); "
        f"[print(f'  {{row[0]}}: ({{row[1]}}, {{row[2]}}, {{row[3]}})') for row in transmitters[:5]]; "
        f"print('✓ Format valid for Sionna simulation')"
    ]
    
    return {
        'transmitter_file': sionna_transmitter_file,
        'output_dir': output_dir,
        'commands': commands,
        'num_transmitters': len(transmitters)
    }

def run_pipeline_integration(building, date_str):
    """
    Run the complete pipeline: data fetch → ML → AP coordinates → Sionna prep.
    
    Parameters
    ----------
    building : str
        Building code (e.g., 'D1')
    date_str : str
        Date in YYYY-MM-DD format
    
    Returns
    -------
    dict
        Pipeline results and next steps
    """
    results = {
        'pipeline_run': False,
        'ml_results': None,
        'ap_coordinates': None,
        'sionna_ready': False,
        'errors': []
    }
    
    # Check if AP prediction pipeline exists
    pipeline_script = "../ap-prediction-automation/run_all.bash"
    if not os.path.exists(pipeline_script):
        results['errors'].append(f"Pipeline script not found: {pipeline_script}")
        return results
    
    print(f"🔄 Running AP prediction pipeline for {building} on {date_str}")
    
    try:
        # Run the ML pipeline
        cmd = [
            "bash", pipeline_script,
            "--building", building,
            "--date", date_str,
            "--output-format", "coordinates"
        ]
        
        print(f"Command: {' '.join(cmd)}")
        result = subprocess.run(cmd, 
                              capture_output=True, 
                              text=True, 
                              cwd="../ap-prediction-automation")
        
        if result.returncode == 0:
            results['pipeline_run'] = True
            print("✓ AP prediction pipeline completed successfully")
            
            # Look for generated coordinate files
            coord_files = []
            data_dir = "../ap-prediction-automation/data"
            if os.path.exists(data_dir):
                for f in os.listdir(data_dir):
                    if f.endswith('.csv') and 'processed' in f:
                        coord_files.append(os.path.join(data_dir, f))
            
            if coord_files:
                # Use the most recent coordinate file
                latest_file = max(coord_files, key=os.path.getmtime)
                results['ap_coordinates'] = latest_file
                print(f"✓ Found AP coordinates: {latest_file}")
                
                # Validate for Sionna compatibility
                is_valid, transmitters, errors = validate_ap_coordinates(latest_file)
                if is_valid:
                    results['sionna_ready'] = True
                    print(f"✓ {len(transmitters)} AP coordinates ready for Sionna")
                else:
                    results['errors'].extend(errors)
            else:
                results['errors'].append("No coordinate files generated by pipeline")
        else:
            results['errors'].append(f"Pipeline failed: {result.stderr}")
            
    except Exception as e:
        results['errors'].append(f"Pipeline execution error: {e}")
    
    return results

def main():
    parser = argparse.ArgumentParser(description="AP Prediction → Sionna Integration Pipeline")
    parser.add_argument('--mode', choices=['validate', 'simulate', 'pipeline'], 
                       required=True, help='Operation mode')
    
    # For validate and simulate modes
    parser.add_argument('--ap_file', type=str, 
                       help='AP coordinate CSV file')
    parser.add_argument('--scene', type=str, 
                       help='Mitsuba scene file (.xml)')
    parser.add_argument('--output_dir', type=str, default='./sionna_output',
                       help='Output directory for simulation')
    
    # For pipeline mode
    parser.add_argument('--building', type=str, 
                       help='Building code (e.g., D1)')
    parser.add_argument('--date', type=str, 
                       help='Date in YYYY-MM-DD format')
    
    args = parser.parse_args()
    
    print("=" * 70)
    print("AP PREDICTION → SIONNA SIMULATION INTEGRATION")
    print("=" * 70)
    
    if args.mode == 'validate':
        if not args.ap_file:
            print("Error: --ap_file required for validate mode")
            return 1
        
        print(f"🔍 Validating AP coordinates: {args.ap_file}")
        is_valid, transmitters, errors = validate_ap_coordinates(args.ap_file)
        
        if is_valid:
            print(f"✅ VALID: {len(transmitters)} AP coordinates ready for Sionna")
            for name, pos in transmitters[:3]:  # Show first 3
                print(f"   {name}: ({pos[0]:.1f}, {pos[1]:.1f}, {pos[2]:.1f})")
            if len(transmitters) > 3:
                print(f"   ... and {len(transmitters) - 3} more")
        else:
            print("❌ INVALID: Issues found:")
            for error in errors:
                print(f"   • {error}")
            return 1
    
    elif args.mode == 'simulate':
        if not args.ap_file:
            print("Error: --ap_file required for simulate mode")
            return 1
        
        print(f"🎯 Preparing Sionna simulation with: {args.ap_file}")
        
        # Validate coordinates
        is_valid, transmitters, errors = validate_ap_coordinates(args.ap_file)
        if not is_valid:
            print("❌ Invalid AP coordinates:")
            for error in errors:
                print(f"   • {error}")
            return 1
        
        # Prepare simulation
        sim_config = prepare_sionna_simulation(transmitters, args.output_dir, args.scene)
        
        print(f"✅ Simulation prepared:")
        print(f"   📁 Output directory: {sim_config['output_dir']}")
        print(f"   📄 Transmitter file: {sim_config['transmitter_file']}")
        print(f"   🎯 Number of APs: {sim_config['num_transmitters']}")
        
        # Run validation
        if 'validate' in sim_config['commands']:
            print("\n🔍 Running format validation...")
            result = subprocess.run(sim_config['commands']['validate'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                print(result.stdout)
            else:
                print(f"Validation warning: {result.stderr}")
        
        # Show simulation commands
        print("\n📋 Next steps:")
        if 'full_simulation' in sim_config['commands']:
            cmd = ' '.join(sim_config['commands']['full_simulation'])
            print(f"   Run simulation: {cmd}")
        else:
            print("   To run full simulation, provide --scene parameter with Mitsuba file")
            cmd = f"python sionna_coverage_map.py --transmitter_file {sim_config['transmitter_file']} --mitsuba_file YOUR_SCENE.xml --output_dir {sim_config['output_dir']}/coverage"
            print(f"   Example: {cmd}")
    
    elif args.mode == 'pipeline':
        if not args.building or not args.date:
            print("Error: --building and --date required for pipeline mode")
            return 1
        
        print(f"🚀 Running complete pipeline: {args.building} on {args.date}")
        
        # Run pipeline integration
        results = run_pipeline_integration(args.building, args.date)
        
        if results['pipeline_run']:
            print("✅ AP prediction pipeline completed")
            
            if results['sionna_ready']:
                print("✅ AP coordinates ready for Sionna simulation")
                print(f"   📄 Coordinate file: {results['ap_coordinates']}")
                
                # Prepare Sionna simulation
                is_valid, transmitters, _ = validate_ap_coordinates(results['ap_coordinates'])
                if is_valid:
                    output_dir = f"./pipeline_output_{args.building}_{args.date.replace('-', '')}"
                    sim_config = prepare_sionna_simulation(transmitters, output_dir)
                    
                    print(f"\n🎯 Sionna simulation ready:")
                    print(f"   📁 Output: {sim_config['output_dir']}")
                    print(f"   🎯 APs: {sim_config['num_transmitters']}")
                    print(f"\n🚀 To run Sionna simulation:")
                    print(f"   python sionna_coverage_map.py \\")
                    print(f"     --transmitter_file {sim_config['transmitter_file']} \\")
                    print(f"     --mitsuba_file YOUR_SCENE.xml \\")
                    print(f"     --output_dir {sim_config['output_dir']}/coverage")
            else:
                print("❌ AP coordinates not compatible with Sionna")
                for error in results['errors']:
                    print(f"   • {error}")
        else:
            print("❌ Pipeline execution failed")
            for error in results['errors']:
                print(f"   • {error}")
            return 1
    
    print("\n" + "=" * 70)
    print("Integration pipeline ready! Your AP coordinates → Sionna simulation workflow is complete.")
    return 0

if __name__ == "__main__":
    exit(main())
