# 🌿 Autonomous Greenhouse Controller

An intelligent agricultural IoT system that monitors environmental variables and automates life-support systems for plants to maximize yield and minimize water waste.

## 🚀 Features
- **Smart Irrigation:** Triggers water pumps only when soil moisture falls below a dynamic threshold.
- **Climate Regulation:** Controls fans and misters based on DHT11 humidity/temperature data.
- **Water Consumption Tracking:** Logs every "Pump Event" to calculate total water usage.
- **Legacy Integration:** Demonstrates IoT capabilities on the Arduino Uno platform via ESP-01.

## ⚙️ Engineering Logic
- **Hardware:** Arduino Uno handles the local sensor-actuator loop (PID-style).
- **Software:** Python analyzes the "Evapotranspiration" rate based on temp/humidity to suggest better watering schedules.
