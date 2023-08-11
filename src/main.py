import machine
import network
import socket
import json
import time
import request_tools
import AHT21
import ENS160
import settings
import NeopixelEngine

# set up
led = machine.Pin("LED", machine.Pin.OUT)
i2c = machine.I2C(0, sda=machine.Pin(12), scl=machine.Pin(13))
aht = AHT21.AHT21(i2c)
ens = ENS160.ENS160(i2c)
ens.operating_mode = 2
neo = NeopixelEngine.NeopixelEngine()


# start up sequence
neo.startup_pattern()

##### VARIABLES #####
aqi:int = 0
co2:int = 0
tvoc:int = 0
humidity:float = 0.0 # relative humidity
temperature:float = 0.0 # celsius
cycles:int = 0
#####################

while True:

    # perform measurements
    print("Measuring AQI...")
    aqi = ens.AQI
    print("AQI: " + str(aqi))
    print("Measuring CO2...")
    co2 = ens.CO2
    print("Measuring TVOC...")
    tvoc = ens.TVOC
    
    # perform measurements - AHT21
    print("Measuring temperature and humidity...")
    rht = aht.read()
    humidity = rht[0]
    temperature = rht[1]

    # set the correct level
    print("Setting level...")
    neo.show_level(min(max(aqi, 1), 5))

    # increment cycle
    cycles = cycles + 1
    print(str(cycles) + " cycles complete!")

    # wait
    print("Waiting 60 seconds...")
    time.sleep(60)