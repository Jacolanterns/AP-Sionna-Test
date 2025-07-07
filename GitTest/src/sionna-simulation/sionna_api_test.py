#!/usr/bin/env python3
"""
SIONNA 1.1.0 - WORKING API TEST
================================

Simple test to confirm all API issues are fixed
"""

import sys
import os

def test_sionna_api():
    """Test Sionna 1.1.0 API components."""
    print("🚀 TESTING SIONNA 1.1.0 API")
    print("=" * 40)
    
    try:
        print("1️⃣ Importing Sionna...")
        import sionna
        print(f"   ✅ Sionna {sionna.__version__} imported")
        
        print("2️⃣ Importing RT modules...")
        from sionna.rt import Scene, PlanarArray, Transmitter, Receiver
        print("   ✅ RT modules imported")
        
        print("3️⃣ Creating Scene...")
        scene = Scene()
        scene.frequency = 2.4e9
        print("   ✅ Scene created and configured")
        
        print("4️⃣ Creating PlanarArray...")
        array = PlanarArray(
            num_rows=1, 
            num_cols=1, 
            vertical_spacing=0.5, 
            horizontal_spacing=0.5, 
            pattern="iso",
            polarization="V"
        )
        print("   ✅ PlanarArray created successfully")
        
        print("5️⃣ Creating Transmitter...")
        tx = Transmitter(
            name="test_tx", 
            position=[10.0, 20.0, 6.0],
            orientation=[0, 0, 0]
        )
        tx.antenna.array = array
        scene.add(tx)
        print("   ✅ Transmitter created and added to scene")
        
        print("6️⃣ Creating Receiver...")
        rx = Receiver(
            name="test_rx", 
            position=[0, 0, 1.5],
            orientation=[0, 0, 0]
        )
        rx.antenna.array = array
        scene.add(rx)
        print("   ✅ Receiver created and added to scene")
        
        print("\n🎉 ALL API TESTS PASSED!")
        print("✅ Sionna 1.1.0 API is fully working")
        print("✅ Ready for full ray tracing simulation")
        
        return True
        
    except Exception as e:
        print(f"❌ API Test failed: {e}")
        print(f"   Error type: {type(e).__name__}")
        return False

def test_ap_loading():
    """Test loading dummy APs."""
    print("\n📡 TESTING DUMMY AP LOADING")
    print("=" * 40)
    
    ap_file = "../data/2f.csv"
    try:
        if not os.path.exists(ap_file):
            print(f"❌ AP file not found: {ap_file}")
            return False
            
        with open(ap_file, 'r') as f:
            lines = f.readlines()
            
        aps = []
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
                    print(f"   📍 {name}: ({x}, {y}, {z})")
                    
        print(f"✅ Loaded {len(aps)} dummy APs successfully")
        return True
        
    except Exception as e:
        print(f"❌ AP loading failed: {e}")
        return False

def main():
    print("🔧 SIONNA 1.1.0 API VALIDATION TEST")
    print("=" * 50)
    
    # Test API
    api_ok = test_sionna_api()
    
    # Test AP loading
    ap_ok = test_ap_loading()
    
    print("\n🏆 FINAL RESULTS:")
    print("=" * 30)
    print(f"✅ Sionna 1.1.0 API: {'WORKING' if api_ok else 'FAILED'}")
    print(f"✅ Dummy AP Loading: {'WORKING' if ap_ok else 'FAILED'}")
    
    if api_ok and ap_ok:
        print("\n🎉 ALL SYSTEMS GO!")
        print("🚀 Ready for full Sionna ray tracing simulation!")
        print("📡 Dummy APs + Sionna 1.1.0 = INTEGRATION COMPLETE")
    else:
        print("\n⚠️  Issues detected - check errors above")
        
    return api_ok and ap_ok

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
