#src -https://github.com/adamjezek98/MPU6050-ESP8266-MicroPython/blob/master/mpu6050.py

import machine

#changed accel() -> imu()
def bytes_toint( firstbyte, secondbyte):
    
    firstbyte = "0"+firstbyte
    secondbyte = "0"+(secondbyte)
    
    firstbyte= hex(int(firstbyte, 16) + 0x200)
    secondbyte = hex(int(secondbyte, 16) + 0x200)
    print( firstbyte," ", secondbyte)
    if not firstbyte & 0x80:
        return firstbyte << 8 | secondbyte
    return - (((firstbyte ^ 255) << 8) | (secondbyte ^ 255) + 1)

    #added passable raw_ints
def get_values(raw_ints):
    #raw_ints = self.get_raw_values()
    vals = {}
    vals["AcX"] = bytes_toint(raw_ints[0], raw_ints[1])
    vals["AcY"] = bytes_toint(raw_ints[2], raw_ints[3])
    vals["AcZ"] = bytes_toint(raw_ints[4], raw_ints[5])
    vals["Tmp"] = bytes_toint(raw_ints[6], raw_ints[7]) / 340.00 + 36.53
    vals["GyX"] = bytes_toint(raw_ints[8], raw_ints[9])
    vals["GyY"] = bytes_toint(raw_ints[10], raw_ints[11])
    vals["GyZ"] = bytes_toint(raw_ints[12], raw_ints[13])
    return vals  # returned in range of Int16
class imu():
    def __init__(self, i2c, addr=0x68):
        self.iic = i2c
        self.addr = addr
        self.iic.start()
        self.iic.writeto(self.addr, bytearray([107, 0]))
        self.iic.stop()

    def get_raw_values(self):
        self.iic.start()
        a = self.iic.readfrom_mem(self.addr, 0x3B, 14)
        self.iic.stop()
        return a

    def get_ints(self):
        b = self.get_raw_values()
        c = []
        for i in b:
            c.append(i)
        return c

    
        # -32768 to 32767

    def val_test(self):  # ONLY FOR TESTING! Also, fast reading sometimes crashes IIC
        from time import sleep
        while 1:
            print(self.get_values())
            sleep(0.05)