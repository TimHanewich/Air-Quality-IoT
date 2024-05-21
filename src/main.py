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
print("Setting up ENS160 and AHT21 interface via I2C...")
i2c = machine.I2C(1, sda=machine.Pin(14), scl=machine.Pin(15))
aht = AHT21.AHT21(i2c)
ens = ENS160.ENS160(i2c)
ens.reset()
time.sleep(0.5)
ens.operating_mode = 2
time.sleep(2.0)

# connect to wifi
print("Preparing for wifi connection...")
wifi_con_attempt:int = 0
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
while wlan.isconnected() == False:

    wifi_con_attempt = wifi_con_attempt + 1

    # blip light
    led.on()
    time.sleep(0.1)
    led.off()
    
    print("Attempt #" + str(wifi_con_attempt) + " to connect to wifi...")
    wlan.connect(settings.ssid, settings.password)
    time.sleep(3)
print("Connected to wifi after " + str(wifi_con_attempt) + " tries!")
my_ip:str = str(wlan.ifconfig()[0])
print("My IP Address: " + my_ip)

# create watchdog timer
wdt = machine.WDT(timeout=8388) # 8,388 ms is the limit (8.388 seconds)
wdt.feed()
print("Watchdog timer now activated.")

# Enter infinite loop
samples_uploaded:int = 0
while True:

    # LED on while we are doing something
    led.on()

    # take reading from ENS160
    print("Taking ENS160 measurements... ")
    aqi:int = ens.AQI
    eco2:int = ens.CO2
    tvoc:int = ens.TVOC
    print("AQI: " + str(aqi) + ", ECO2: " + str(eco2) + ", TVOC: " + str(tvoc))
    wdt.feed()

    # if there was an error getting legit values from the ENS160
    if aqi == 0 or eco2 == 0 or tvoc == 0:
        print("AQI, ECO2, or TVOC readings were not successful! Going into troubleshooting mode.")
        while aqi == 0 or eco2 == 0 or tvoc == 0: # go into troubleshooting mode, trying to recover ENS160 functionality, until solved for.

            # print msg
            print("AQI/ECO2/TVOC reading unsuccessful at last attempt. Will try to reset again.")

            # flash quickly to show an issue
            print("Playing troubleshooting LED pattern...")
            for x in range(0, 5): 
                led.on()
                time.sleep(0.05)
                led.off()
                time.sleep(0.05)
                wdt.feed()
            
            print("Resetting ENS160...")
            ens.reset() # reset
            wdt.feed() # feed watchdog timer
            
            # take sample
            print("Sampling ENS160 after reset...")
            time.sleep(1)
            led.on()
            aqi = ens.AQI
            eco2 = ens.CO2
            tvoc = ens.TVOC
            wdt.feed()
            led.off()
    
    # take reading from AHT21
    print("Taking AHT21 measurements...")
    rht = aht.read()
    humidity:float = rht[0]
    humidity = humidity / 100
    temperature:float = rht[1]
    wdt.feed()

    # create json body
    body = {"aqi": aqi, "eco2": eco2, "tvoc": tvoc, "humidity": humidity, "temperature": temperature}
    print("Measurements taken! " + str(body))
    wdt.feed()
    
    # make HTTP call
    print("Making HTTP call...")
    wdt.feed()
    pr = urequests.post(settings.post_url, json=body)
    wdt.feed()
    pr.close()
    print("HTTP call made!")

    # if the status code of the HTTP response was not succesful (not in the 200 range), go into an infinite loop of
    # This is here so the program will stop if, for example, the receiving endpoint is no longer active or accepting.
    if str(pr.status_code)[0:1] != "2":
        while True: 
            led.on()
            wdt.feed()
            time.sleep(1)
            led.off()
            wdt.feed()
            time.sleep(1)
    else:
        print("Sample upload successfully accepted!")

    # increment tracker
    samples_uploaded = samples_uploaded + 1

    # wait for time
    led.off() # led off while doing nothing (just waiting)
    next_loop:int = time.ticks_ms() + (1000 * settings.sample_time_seconds)
    while (time.ticks_ms() < next_loop):
        print("Sampling #" + str(samples_uploaded + 1) + " next in " + str(round((next_loop - time.ticks_ms()) / 1000, 0)) + " seconds...")
        time.sleep(1)
        wdt.feed()