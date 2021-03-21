from imuDataStruct import IMUDataVector
from fusion import Fusion
#from I2Chandler_for_mpu6050 import mpu6050Handler
from classHandler import ClassHandler
 
class FusionHandler(ClassHandler):
    #dict_data_in
    def __init__(self,accel_gyro_vect = IMUDataVector()):
        self.accel_gyro_vect = accel_gyro_vect
        self.fuse_obj = Fusion()
        
    def Update(self,vect_in):
        #print(vect_in)
        self.accel_gyro_vect = vect_in
        #print(self.accel_gyro_vect)
        self.fuse_obj.update_nomag(self.accel_gyro_vect.getAccel(), self.accel_gyro_vect.getAccel()) # Note blocking mag read
        #fuse.heading, fuse.pitch, fuse.roll
        #print(self.fuse_obj.heading,self.fuse_obj.heading,self.fuse_obj.roll)
        return (self.fuse_obj.heading,self.fuse_obj.heading,self.fuse_obj.roll)