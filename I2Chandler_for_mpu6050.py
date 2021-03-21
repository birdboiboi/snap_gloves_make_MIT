from machine import Pin, SoftI2C
from MPU6050 import imu
from I2Chandler import I2c_MOD_Single_Soft
from imuDataStruct import IMUDataVector
from fusionHandler import FusionHandler
from fusion import Fusion


class mpu6050Handler(I2c_MOD_Single_Soft):
    data = None
    read_addr = 0x69
    on_off= False
    parsedValue = None
    vect_data = IMUDataVector()
    fuse = FusionHandler()
    polar_coord_tup = None
    def __init__(self,name = "no name",
                 pin_out =[],
                 pin_in=[],
                 pull_up=[],
                 pull_down=[],
                 freq=57600,
                 byteBuffer = 10 ):
        super(mpu6050Handler,self).__init__(name = name,pin_out = pin_out,pin_in =pin_in,pull_up=pull_up,pull_down=pull_down)
        print(self)
        self.pin_out = pin_out
        self.pin_in = pin_in
        self.pull_up =pull_up
        self.pull_down = pull_down
        self.freq = freq
        self.Start()
        self.sda=self.pin_mac_in[0]
        self.scl=self.pin_mac_out[0]
        self.ado =  self.pin_mac_out[1]
        print(self.sda,self.scl,self.ado)
        self.I2c_object = SoftI2C(scl = self.scl,sda = self.sda,freq = self.freq)
        self.mpu6050_imu = imu( self.I2c_object, addr=0x69,handler=self)
        self.byteBuffer = byteBuffer
        
        
    def Read(self):
        self.data=(self.mpu6050_imu.get_values())
        self.vect_data = IMUDataVector(self.data) 
        self.polar_coord_tup = self.fuse.Update(self.vect_data)
        #print(self.name,"\n",self.vect_data,"polar_coord_tup",self.polar_coord_tup)
        
    def parse(self):
        super(mpu6050Handler,self).parse()
        #parsedValue = self.data.split("\\")
        self.parsedValue = MPU6050.get_values(self.parsedValue[1:])
        print(self.parsedValue)