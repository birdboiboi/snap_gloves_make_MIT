import sampleCode as sc
import time
import os

#
import classHandlerList as CHL
class_handler_list = CHL.get_list_of_imports()


class Main:
    def __init__(self):
        print("****************program*************")
        Boot
        
    def Boot():
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
                i.Update()
        
    def Loop(self):
        while 1==1:
            for i in class_handler_list:
                i.Update()
        time.sleep_ms(125)
        #self.Loop() #for recursion
            
#p = Main()