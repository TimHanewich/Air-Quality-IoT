import machine
import time
i2c = machine.I2C(0, sda=machine.Pin(12), scl=machine.Pin(13))
print(i2c.scan())
addr = 0x53

# read device id
#id = i2c.readfrom_mem(addr, 0x00, 2)
#print(id)

# read operating mode
#op_mode = i2c.readfrom_mem(addr, 0x10, 1)
#print(op_mode)

# read int config
#op_mode = i2c.readfrom_mem(addr, 0x11, 1)
#print(op_mode)

# set operating mode
#i2c.writeto_mem(addr, 0x10, bytes([0x02]))

# write to turn off interupt pin
#i2c.writeto_mem(addr, 0x11, bytes([2]))

# read co2
#co2 = i2c.readfrom_mem(addr, 0x24, 2)
#print(co2)




# EMULATING BEGIN
#i2c.writeto_mem(addr, 0x10, bytes([0x02]))
#time.sleep(1.0)
#mode = 0x00
#v_en = 1<<1 # enable
#v_dis = 0<<1 # disable
#mode |= ( v_en | v_dis)
#i2c.writeto_mem(addr, 0x11, bytes([mode]))
#time.sleep(1.0)
#co2 = i2c.readfrom_mem(addr, 0x24, 2)
#print(co2)