import machine
import network
import time
import AHT21
import ENS160
import settings
import urequests

# boot pattern
led = machine.Pin("LED", machine.Pin.OUT)
print("Playing LED boot pattern...")
led.on()
time.sleep(0.5)
led.off()
time.sleep(0.5)
led.on()
time.sleep(0.5)
led.off()
time.sleep(0.5)
led.on()
time.sleep(0.5)
led.off()
time.sleep(0.5)

# set up
i2c = machine.I2C(1, sda=machine.Pin(14), scl=machine.Pin(15))
aht = AHT21.AHT21(i2c)
ens = ENS160.ENS160(i2c)
ens.reset()
time.sleep(0.5)
ens.operating_mode = 2
time.sleep(2.0)

# connect to wifi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
while wlan.isconnected() == False:

    # blip light
    led.on()
    time.sleep(0.1)
    led.off()
    
    print("Attemping to connect to wifi...")
    wlan.connect(settings.ssid, settings.password)
    time.sleep(3)
print("Connected to wifi!")
my_ip:str = str(wlan.ifconfig()[0])
print("My IP Address: " + my_ip)

# Enter infinite loop
while True:

    # take reading from ENS160
    print("Taking ENS160 measurements... ")
    aqi:int = ens.AQI
    eco2:int = ens.CO2
    tvoc:int = ens.TVOC
    
    # take reading from AHT21
    print("Taking AHT21 measurements...")
    rht = aht.read()
    humidity:float = rht[0]
    humidity = humidity / 100
    temperature:float = rht[1]

    # create json body
    body = {"aqi": aqi, "eco2": eco2, "tvoc": tvoc, "humidity": humidity, "temperature": temperature}
    print("Measurements taken! " + str(body))
    
    # make HTTP call
    print("Making HTTP call...")
    pr = urequests.post(settings.post_url, json=body)
    pr.close()
    print("HTTP call made!")

    # wait
    print("Now waiting for " + str(settings.sample_time_seconds) + " seconds...")
    time.sleep(settings.sample_time_seconds)