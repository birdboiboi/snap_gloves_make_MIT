import sampleCode as sc
import time
import os

#
import clientHandler
import classHandlerList as CHL
class_handler_list = CHL.get_list_of_imports()
def run(machineName = None):
    p = Main(machineName)

class Main:
    def __init__(self,this_mac_name = None):
        print("****************program*************")
        self.this_mac_name = this_mac_name
        self.Boot()
        
    def Boot(self):
        for i in class_handler_list:
            try:
                i.isTypeCH == True
            except:
                print(i,"faulty")
                class_handler_list.remove(i)
        self.Setup()
        self.Loop()
        
    def Setup(self):
        print("runs once")
        for i in class_handler_list:
            if type(i) == clientHandler.ClientHandler:
                
                i.name = self.this_mac_name
                print(i)
            print(i)
            i.Start()
                
        
    def Loop(self):
        while 1==1:
            for i in class_handler_list:
                if not i.suppress:
                    i.Update()
                    print(i)
            print("next frame")
            time.sleep_ms(50)
        #self.Loop() #for recursion
            
#p = Main()