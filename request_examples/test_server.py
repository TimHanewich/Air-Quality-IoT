import network
import socket
import time
import select

# connect to wifi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
while wlan.isconnected() == False:    
    print("Attemping to connect to wifi...")
    wlan.connect("Marco Polo", "Madeleine2002!")
    time.sleep(3)
print("Connected to wifi!")
my_ip:str = str(wlan.ifconfig()[0])
print("My IP Address: " + my_ip)

# start listening
addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
s.setblocking(True)
while True:
    
    print("Awaiting connection...")
    cl, addr = s.accept()
    print("Connection from " + addr[0] + "!")
    
    # collect bytes (non blocking)
    cl.settimeout(1.5)
    data = bytearray()
    while True:
        print("Collecting a few bytes...")
        try:
            buff = cl.recv(5)
            data.extend(buff)
        except Exception as e:
            print("Byte collection did not work! Msg: " + str(e))
            break
    
    
    print(str(len(data)) + " bytes received")
    
    # print all data
    print(data.decode())
    
    # respond with OK
    cl.send("HTTP/1.0 200 OK\r\nContent-Type: application/json\r\n\r\n{\"time\": \"" + str(time.ticks_ms()) + "\"}")
    cl.close()
