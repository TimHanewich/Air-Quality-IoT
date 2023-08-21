import machine
import network
import socket
import json
import time
import request_tools
import AHT21
import ENS160
import settings


# set up
led = machine.Pin("LED", machine.Pin.OUT)
i2c = machine.I2C(0, sda=machine.Pin(12), scl=machine.Pin(13))
aht = AHT21.AHT21(i2c)
ens = ENS160.ENS160(i2c)
ens.operating_mode = 2

# boot pattern
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

# start listening
addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
led.on()
while True:
    print("Awaiting connection...")
    cl, addr = s.accept()
    print("Connection from " + addr[0] + "!")
    
    try:

        # collect bytes
        data = request_tools.read_all(cl, 500)
        print(str(len(data)) + " bytes received")
        
        # parse
        req = request_tools.request.parse(data.decode())
        
        if req.method.lower() == "get" and req.path.lower() == "/data":
            print("It is a request for data")
            
            # perform measurements
            print("Measuring AQI...")
            aqi = ens.AQI
            print("Measuring CO2...")
            co2 = ens.CO2
            print("Measuring TVOC...")
            tvoc = ens.TVOC
            
            # perform measurements - AHT21
            print("Measuring temperature and humidity...")
            rht = aht.read()
            humidity = rht[0]
            temperature = rht[1]
            
            ReturnObj = {"aqi": aqi, "co2": co2, "tvoc": tvoc, "humidity": humidity, "temperature": temperature}
            
            # respond with OK
            print("Responding...")
            cl.send("HTTP/1.0 200 OK\r\nContent-Type: application/json\r\nAccess-Control-Allow-Origin: *\r\n\r\n" + json.dumps(ReturnObj))
            cl.close()
            print("Responded!")
            
        elif req.method.lower() == "get" and req.path.lower() == "/":
            
            f = open("page.html")
            content = f.read()
            f.close()
            
            # respond with OK
            cl.send("HTTP/1.0 200 OK\r\nContent-Type: text/html\r\n\r\n" + content)
            cl.close()
            
        else:
            cl.send("HTTP/1.0 404 NOT FOUND\r\n\r\n");
            cl.close();            
        
    except Exception as e:
        print("Fatal error! Msg: " + str(e))
        cl.send("HTTP/1.0 500 INTERNAL SERVER ERROR\r\n\r\n")
        cl.close()
        
    
    
    
    
    
    