from MPU6050 import imu
from I2Chandler import I2c_MOD_Single_Soft

class mpu6050Handler(I2c_MOD_Single_Soft):
    def __init__(self,name = "no name",
                     pin_out =[],
                     pin_in=[],
                     pull_up=[],
                     pull_down=[],
                     freq=57600;
                     byteBuffer=14
                      ):
        super(I2c_MOD_Single_Hard,self).__init__(name = name,pin_out = pin_out,pin_in =pin_in,pull_up=pull_up,pull_down=pull_down)
        
        self.pin_out = pin_out
        self.pin_in = pin_in
        self.pull_up =pull_up
        self.pull_down = pull_down
        self.freq = freq
        self.Start()
        self.sda=self.pin_mac_out[0]
        self.scl=self.pin_mac_out[0]
        self.ado =  self.pin_mac_out[1]
        self.byteBuffer = byteBuffer
        