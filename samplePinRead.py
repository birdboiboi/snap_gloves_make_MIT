from machine import Pin
import classHandler

class SamplePinRead(classHandler.ClassHandler):
    pin_out= None
    pin_in= None
    pull_up= None
    pull_down= None
    pin_mac_out = []
    pin_mac_in =[]
    read_pins= []
    write_vals= []
    read_len= None
    write_len= None
    def __init__(self,name = "no name",
                 pin_out =[],
                 pin_in=[],
                 pull_up=[],
                 pull_down=[]):
        super(SamplePinRead, self).__init__()
        self.name = name
        self.pin_out = pin_out
        self.pin_in = pin_in
        self.pull_up =pull_up
        self.pull_down = pull_down
        
    def Start(self):
        self.Setup_Pins_Out()
        self.Setup_Pins_In()
        
        
    def Setup_Pins_Out(self):
        for pin_num in self.pin_out:
            if pin_num in self.pull_up:
                self.pin_mac_out.append(Pin(pin_num,Pin.OUT,Pin.PULL_UP))
            elif pin_num in self.pull_down:
                self.pin_mac_out.append(Pin(pin_num,Pin.OUT,Pin.PULL_DOWN))
            else:
                self.pin_mac_out.append(Pin(pin_num,Pin.OUT))
            self.write_len = len(self.pin_mac_out)
        self.write_vals = [None] * self.write_len
            
    def Setup_Pins_In(self): 
        for pin_num in self.pin_in:
            if pin_num in self.pull_up:
                self.pin_mac_in.append(Pin(pin_num,Pin.IN,Pin.PULL_UP))
            elif pin_num in self.pull_down:
                self.pin_mac_in.append(Pin(pin_num,Pin.IN,Pin.PULL_DOWN))
            else:
                self.pin_mac_in.append(Pin(pin_num,Pin.IN))
        self.read_len = len(self.pin_mac_in)
        self.read_pins = [None] * self.read_len
        #print("set up complete")
        #print(self.name,self.read_pins)
            
    def Read(self):
        print("Read")
        for pin_num in range(0,self.read_len):
            print("pin num",pin_num)
            #print(self.pin_mac_in[pin_num])
            #print(self.read_pins)
            self.read_pins[pin_num] = self.pin_mac_in[pin_num].value()
        
    def Write(self):
        for pin_num in range(0,self.write_len):
            self.pin_mac_out[pin_num].value(self.write_vals[pin_num])
            
    def Update(self):
        #print("len",self.read_len)
        #print(self.read_pins)
        self.Read()
    def __str__(self):
        return ("(" , str(self.write_vals), " write to " ,self.pin_mac_out , ") (", self.read_pins, " reads " ,self.pin_mac_in) 