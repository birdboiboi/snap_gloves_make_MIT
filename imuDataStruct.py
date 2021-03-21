
class IMUDataVector ():
    CONST_ONES_TUPLE = (1,1,1)
    CONST_ZEROS_TUPLE = (0,0,0)
    def __init__(self,dict_data_in = None,gyro_tuple_init = (0,0,0),accel_tuple_init  = (0,0,0)):
        if dict_data_in != None:
            self.gX = dict_data_in["GyX"]
            self.gY = dict_data_in["GyY"]
            self.gZ = dict_data_in["GyZ"]
            self.aX = dict_data_in["AcX"]
            self.aY = dict_data_in["AcY"]
            self.aZ = dict_data_in["AcZ"] 
        else:
            
            self.update(gyro_tuple = tuple(gyro_tuple_init),accel_tuple = tuple(accel_tuple_init))
            
    def update(self,gyro_tuple = None,accel_tuple = None):    
        self.gX = gyro_tuple[0]
        self.gY = gyro_tuple[1]
        self.gZ = gyro_tuple[2]
        self.aX = accel_tuple[0]
        self.aY = accel_tuple[1]
        self.aZ = accel_tuple[2]
        
    def getAccel(self):
        return (self.aX,self.aY,self.aZ)
    
    def getGyro(self):
        return (self.gX,self.gY,self.gZ)
        
    def getAccelMag(self):
        return self.getMag(self.aX,self.aY,self.aZ)
        
    def getGyroMag(self):
        return self.getMag(self.gX,self.gY,self.gZ)
        
    def getAccelNormalized(self):
        return self.getNormalized(self.aX,self.aY,self.aZ)
        
    def getGyroNormalized(self):
        return self.getNormalized(self.gX,self.gY,self.gZ)
        
    def add(self,other):
        sum_gyro = (self.gX + other.gX,self.gY + other.gY,self.gZ + other.gZ)
        sum_accel = (self.aX + other.aX,self.aY + other.aY,self.aZ + other.aZ)
        
        return IMUDataVector(gyro_tuple=sum_gyro,accel_tuple=sum_accel)
    
    def scale(scalar = None,other = None):
        if scalar != None:
            other = (scalar,scalar,scalar)
        prod_accel = (self.aX * other.aX,self.aY * other.aY,self.aZ * other.aZ)
        prod_gyro = (self.gX * other.gX,self.gY * other.gY,self.gZ * other.gZ)
        return IMUDataVector(gyro_tuple=prod_gyro,accel_tuple=prod_accel)
    
    def getMag(self,x,y,z):
        return ((x**2)+(y**2)+(z**2))**(1/2)
    
    def getNormalized(self,x,y,z):
        mag = self.getMag(x,y,z)
        return (x/mag,y/mag,z/mag)
        
    def __str__(self):
        return ("accel<",self.getAccel(),">gyro<",self.getGyro(),">")
        
    