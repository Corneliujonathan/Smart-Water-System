"""
Project: Smart Water Management System (Simulation)
Author: Corneliu Jonathan
Date: 2024
Description: 
    This script simulates the IoT firmware logic. It generates mock sensor data 
    (pH & Turbidity), validates it against safety thresholds, and simulates 
    cloud data transmission.
"""
import time
import random

# --- CONFIGURATION ---
# In the real project, these values came from sensors.
# Here, we verify the LOGIC.
PH_THRESHOLD_MIN = 6.5
PH_THRESHOLD_MAX = 8.5
TURBIDITY_THRESHOLD = 5.0

def read_sensor_data():
    """
    Simulates reading data from hardware sensors.
    In the real device, this would use GPIO pins.
    """
    # Generating random values to simulate water quality
    current_ph = round(random.uniform(5.0, 9.0), 2)
    current_turbidity = round(random.uniform(1.0, 10.0), 2)
    return current_ph, current_turbidity

def send_to_cloud(ph, turbidity, status):
    """
    Simulates sending data to ThingSpeak Cloud API.
    """
    print(f"[CLOUD UPLOAD] Sending Data -> pH: {ph} | Turbidity: {turbidity} | Status: {status}")
    # Real code would use: requests.get(url)
    time.sleep(1) # Simulating network delay

def check_quality(ph, turbidity):
    """
    The Core Logic: Decides if water is safe or spoiled.
    """
    if ph < PH_THRESHOLD_MIN or ph > PH_THRESHOLD_MAX:
        return "CRITICAL: Bad pH Level"
    elif turbidity > TURBIDITY_THRESHOLD:
        return "CRITICAL: Water too cloudy (Turbidity)"
    else:
        return "SAFE: Water Quality Good"

# --- MAIN SYSTEM LOOP ---
print("--- STARTING SMART WATER MANAGEMENT SYSTEM (SIMULATION) ---")

try:
    while True:
        # 1. Get Input
        ph_val, turb_val = read_sensor_data()
        
        # 2. Process Logic
        status_message = check_quality(ph_val, turb_val)
        
        # 3. Output / Alert
        print(f"\nSensor Reading: pH={ph_val} | Turbidity={turb_val}")
        print(f"System Status: {status_message}")
        
        # 4. Upload to Cloud
        send_to_cloud(ph_val, turb_val, status_message)
        
        # Wait for 3 seconds before next reading
        time.sleep(3)

except KeyboardInterrupt:

    print("\nSystem Stopped by User.")
