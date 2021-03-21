from machine import Pin, I2C
from samplePinRead import SamplePinRead
from I2Chandler import I2c_MOD_Single_Soft
from I2Chandler_mac import I2c_MOD_Single_Hard
from I2Chandler_for_mpu6050 import mpu6050Handler
from classHandler import ClassHandler
import time

#GPIO 21 - , GPIO
class I2c_MOD_Multi(SamplePinRead):
    #HARD_I2C = [21,22]
    HARD_I2C = []
    i2c_list= []
    suppress_print = False
    def __init__(self,name = "no name",
                 pin_out =[],
                 pin_in=[],
                 pull_up=[],
                 pull_down=[],
                 freq=100000,
                 byteBuffer = 14,
                 pass_names = []                 ):
        super(I2c_MOD_Multi,self).__init__(name = name,pin_in = pin_in,pull_up = pull_up,pull_down = pull_down)
        self.pin_out = pin_out
        self.pin_in = pin_in
        self.pull_up =pull_up
        self.pull_down = pull_down
        print(self.name)
        print(self.pin_in)
        self.freq = freq
        self.byteBuffer = byteBuffer
        self.pass_names = pass_names
        
    def Start(self):
        #2 outputs and #1 input
        print("init pins for I2c",len(self.pin_in),len(self.pin_in))
        for i in range(0,len(self.pin_in)):
            j = i+1
            add_in = [self.pin_in[i]]
            add_out = [self.pin_out[j-1],self.pin_out[j]]
            try:
                name_2_pass = self.pass_names[i]
            except:
                name_2_pass = "I2c_MOD_Single_Soft "+str(i)
            #if (( (self.HARD_I2C[0] in add_in) ) or ((self.HARD_I2C[0] in add_out) )) or ((self.HARD_I2C[1] in add_in) ) or ((self.HARD_I2C[1] in add_out)):#([0, 40] == a).all(1).any()
            #    print("use hardware")
            #    self.i2c_list.append(I2c_MOD_Single_Hard(name = "I2c_MOD_Single_Hard "+str(i),
            #                                            pin_in= add_in,
            #                                            pin_out=add_out,
            #                                            pull_up = self.pull_up,
            #                                            pull_down = self.pull_down,
            #                                            freq = self.freq,
            #                                            byteBuffer = self.byteBuffer))
            #else:
            self.i2c_list.append(mpu6050Handler(name = name_2_pass,
                                                        pin_in= add_in,
                                                        pin_out=add_out,
                                                        pull_up = self.pull_up,
                                                        pull_down = self.pull_down,
                                                        freq = self.freq,
                                                        byteBuffer = self.byteBuffer))
                                                        
    def Update(self):
       
        for I2c_mod in self.i2c_list:
            I2c_mod.toggle_on_off()
            #print()
            #time.sleep_ms(500)
            I2c_mod.Read()
            I2c_mod.toggle_on_off()
            I2c_mod.parse()
            
    
    def __str__(self):
        if not self.suppress_print:
            string_2_print = self.name+ ": "
            for I2c_mod in self.i2c_list:
                string_2_print = string_2_print+ I2c_mod.name + I2c_mod.data +":"
            return string_2_print