#!/usr/bin/env python3
"""
SIONNA 1.1.0 - ANTENNA API DISCOVERY
====================================

Quick test to find the correct antenna assignment method
"""

import sys
import os

def test_antenna_methods():
    """Try different antenna assignment approaches."""
    print("🔍 Testing Antenna Assignment Methods...")
    
    try:
        from sionna.rt import Scene, PlanarArray, Transmitter
        
        # Create components
        scene = Scene()
        array = PlanarArray(num_rows=1, num_cols=1, vertical_spacing=0.5, 
                           horizontal_spacing=0.5, pattern="iso", polarization="V")
        tx = Transmitter(name="test_tx", position=[10.0, 20.0, 6.0])
        
        print("✅ Components created")
        
        # Method 1: Check if antenna is set via Scene
        scene_methods = [m for m in dir(scene) if 'antenna' in m.lower()]
        print(f"Scene antenna methods: {scene_methods}")
        
        # Method 2: Check if transmitters have different constructor
        try:
            # Maybe antenna is passed during construction?
            tx2 = Transmitter(name="test_tx2", position=[10.0, 20.0, 6.0], antenna=array)
            print("✅ Method 2: Antenna in constructor works!")
            return True
        except Exception as e:
            print(f"❌ Method 2 failed: {e}")
        
        # Method 3: Check if scene has antenna setting methods
        if hasattr(scene, 'set_antenna'):
            scene.set_antenna(tx, array)
            print("✅ Method 3: scene.set_antenna works!")
            return True
        
        # Method 4: Check if add method takes antenna
        try:
            scene.add(tx, antenna=array)
            print("✅ Method 4: scene.add with antenna works!")
            return True
        except Exception as e:
            print(f"❌ Method 4 failed: {e}")
            
        # Method 5: Try tx.set_antenna if it exists
        if hasattr(tx, 'set_antenna'):
            tx.set_antenna(array)
            print("✅ Method 5: tx.set_antenna works!")
            return True
            
        print("❌ No working antenna assignment method found")
        return False
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

def main():
    print("🔧 SIONNA 1.1.0 ANTENNA API DISCOVERY")
    print("=" * 50)
    
    success = test_antenna_methods()
    
    if success:
        print("\n🎉 ANTENNA API FIXED!")
        print("✅ Ready for full Sionna ray tracing")
    else:
        print("\n⚠️  Antenna API still needs investigation")
        print("💡 Falling back to working simulation methods")
        
    return success

if __name__ == "__main__":
    main()
