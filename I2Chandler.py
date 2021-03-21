from machine import Pin, SoftI2C
from samplePinRead import SamplePinRead
import time
#GPIO 21 - , GPIO
class I2c_MOD_Single_Soft(SamplePinRead):
    data = ""
    read_addr = 0x69
    on_off= False
    parsedValue = ""
    def __init__(self,name = "no name",
                 pin_out =[],
                 pin_in=[],
                 pull_up=[],
                 pull_down=[],
                 freq=100000,
                 byteBuffer = 14 ):
        super(I2c_MOD_Single_Soft,self).__init__(name = name,pin_out = pin_out,pin_in =pin_in,pull_up=pull_up,pull_down=pull_down)
        self.pin_out = pin_out
        self.pin_in = pin_in
        self.pull_up =pull_up
        self.pull_down = pull_down
        self.freq = freq
        self.Start()
        self.sda=self.pin_mac_in[0]
        self.scl=self.pin_mac_out[0]
        self.ado =  self.pin_mac_out[1]
        self.ado.off()
        print(self.sda,self.scl,self.ado)
        self.I2c_object = SoftI2C(scl = self.scl,sda = self.sda,freq = self.freq)
        self.byteBuffer = byteBuffer
        
        
    def toggle_on_off(self):
        self.on_off = not self.on_off
        if self.on_off:
            self.ado.value(1)
        else:
            self.ado.value(0)
        print(self.ado.value())
            
    def Read(self):
        print("scan")
        print(self.I2c_object.scan() )
        time.sleep(0.5)
        #print("readFrom",self.read_addr) 
        #print(self.I2c_object.readfrom(105, self.byteBuffer))
        #self.I2c_object.stop()
        print("readFrom-mem",self.read_addr) 
        self.I2c_object.start()
        time.sleep(0.5)
        self.data=str(self.I2c_object.readfrom_mem(105,0x3B, self.byteBuffer) ) 
        self.I2c_object.stop()
        print(self.data)
    
    def parse(self):
        self.parsedValue = self.data.split("\\")
        print(self.parsedValue)
         
        #return self.data