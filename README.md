# 💧 Smart Water Management System (Simulation)

### 📌 Project Overview
This repository contains the **backend logic** for an IoT-based Water Quality Monitoring System. The original project utilized hardware sensors (pH and Turbidity) connected to a microcontroller. This Python script demonstrates the **algorithm and decision-making logic** used to process that sensor data.

### ⚙️ How It Works
The system operates on a continuous loop:
1.  **Data Acquisition:** Simulates reading raw data from pH and Turbidity sensors.
2.  **Validation Logic:** Compares readings against safety thresholds defined in the configuration.
    * *Safe pH Range:* 6.5 - 8.5
    * *Max Turbidity:* 5.0
3.  **Alerting:** Determines if the water status is `SAFE` or `CRITICAL`.
4.  **Cloud Integration:** Formats the data packet for upload to the IoT Cloud (ThingSpeak).

### 🛠️ Technical Concepts Used
* **Python 3:** Core programming.
* **Modular Functions:** Clean code structure separating logic from execution.
* **Exception Handling:** Graceful system exit using `try/except`.
* **Conditional Logic:** Nested `if/else` statements for safety checks.

### 🚀 Usage
Run the script to see the simulation in real-time:
```bash
python water_monitor.py
