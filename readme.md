# 😷 Home Indoor Air Quality Sensor IoT Project 🫁
Welcome to my open-source Air Quality Sensor IoT Project! This project monitors your home's indoor air quality in real-time using IoT technology and feeds you data in JSON over a web server.

This project includes: 
- A web server, written in Python, running on a **Raspberry Pi Pico W**.
- An **ENS160 Digital Metal Oxide Multi-Gas Sensor**, used for monitoring **Carbon Dioxide (CO2)**, **Total Volatile Organic Compounds (TOVC)**, and the **Air Quality Index (AQI)** of your home via the I2C protocol.
- An **AHT21 Integrated Temperature and Humidity Sensor**, used for monitoring ambient **temperature** and **humidity** of your home via the I2C protocol.
- A 3D-printed housing box for the Raspberry Pi Pico W and sensors (optional).

I am using a single breakout board that contains both an ENS160 and AHT21 on one board, found [here](https://www.amazon.com/gp/product/B0BXGZCSWG/ref=ppx_yo_dt_b_asin_title_o03_s00).

The Raspberry Pi Pico, along with the ENS160 + AHT20 sensor breakout board live neatly in a small 3D-printed enclosure:
![plugged in](https://i.imgur.com/8NYAxq0.jpg)


## Web Service
The web server (written in Python) that runs on the Raspberry Pi Pico W provides two services. Firstly, the `/data` endpoint performs a reading of the **Carbon Dioxide (CO2)**, **Total Volatile Organic Compounds (TVOC)**, **Air Quality Index (AQI)**, **temperature**, and **humidity** via the onboard ENS160 and AHT21 sensors and returns the data as JSON.

Data endpoint (API):  
![data endpoint](https://i.imgur.com/C1Tsal0.png)

The second service the web server provides is a [full HTML web page](./src/page.html) that can be rendered in any internet browser. The HTML page comes with client-side JavaScript that consumes the `/data` endpoint mentioned above and displays it in a simple UI.

Web page rendered in browser:  
![web page](https://i.imgur.com/IKfawIU.png)

## 3D Printed Housing
I modeled a simple housing tray for the microcontroller and sensors required for this project. You can download the 3D Model (STL file) [here directly from this GitHub repo](https://github.com/TimHanewich/air-quality-box/releases/download/2/aqb_v1.stl).
![3d printed housing](https://i.imgur.com/vjyKvC5.png)
![tray](https://i.imgur.com/bcAuU1n.jpg)

## [Power Platform Extension](./power_platform/)
![pp](https://i.imgur.com/aTbNb3F.png)  
I further extended this project into the No-Code/Low-Code Realm using Microsoft's Power Platform. 

Using an **on-premises gateway** for brokering communication between the Azure cloud (Power Platform) and my air quality sensor web server on my local network, I developed a **custom connector**, **Dataverse table**, **model-driven app**, and **scheduled Power Automate** workflow to collect data, accompanied with an **interactive Power BI dashboard** for data visualization.

You can read more about the Power Platform integration portion of this project [here](./power_platform/).