# 😷 Home Indoor Air Quality Sensor IoT Project 🫁
Welcome to my open-source Air Quality Sensor IoT Project! This project monitors your home's indoor air quality in real-time using IoT technology and feeds you data in JSON over a web server.

This project includes: 
- A data sampling and upload script, written in MicroPython, running on a **Raspberry Pi Pico W**.
- An **ENS160 Digital Metal Oxide Multi-Gas Sensor**, used for monitoring **Carbon Dioxide (CO2)**, **Total Volatile Organic Compounds (TOVC)**, and the **Air Quality Index (AQI)** of your home via the I2C protocol.
- An **AHT21 Integrated Temperature and Humidity Sensor**, used for monitoring ambient **temperature** and **humidity** of your home via the I2C protocol.
- A 3D-printed housing box for the Raspberry Pi Pico W and sensors (optional).

I am using a single breakout board that contains both an ENS160 and AHT21 on one board, found [here](https://www.amazon.com/gp/product/B0BXGZCSWG/ref=ppx_yo_dt_b_asin_title_o03_s00).

The Raspberry Pi Pico, along with the ENS160 + AHT20 sensor breakout board live neatly in a small 3D-printed enclosure:
![plugged in](https://i.imgur.com/8NYAxq0.jpg)

## 3D Printed Housing
I modeled a simple housing tray for the microcontroller and sensors required for this project. You can download the 3D Model (STL file) [here directly from this GitHub repo](https://github.com/TimHanewich/air-quality-box/releases/download/2/aqb_v1.stl).
![3d printed housing](https://i.imgur.com/vjyKvC5.png)
![tray](https://i.imgur.com/bcAuU1n.jpg)

## May 2024 Update
In May 2024, I changed the core functionality of how the Raspberry Pi Pico W performs: instead of being a server, responding to HTTP requests, it now instead samples data at a regular interval and uploads this via POST request to a defined endpoint. 

All of the code and literature behind this old verison can still be found by reverting to commit `3d04d5e89972443a98873347cb8421cb2e6d45a3`.