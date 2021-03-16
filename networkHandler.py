import classHandler
import network
class NetworkHandler(classHandler.ClassHandler):
    #https://docs.micropython.org/en/latest/esp8266/tutorial/network_basics.html
    def __init__(self,name=None,wifi_name = None,password = None):
        super(NetworkHandler, self).__init__()
        self.name=name
        self.wifi_name = wifi_name
        self.password = password
        self.ip_info = ["not set up yet"]
        
    def Start(self):
        sta_if = network.WLAN(network.STA_IF) 
        print (sta_if)
        if not sta_if.isconnected() and self.wifi_name != None and self.password != None:
            print('connecting to network...')
            sta_if.active(True)
            sta_if.connect(self.wifi_name, self.password)
            while not sta_if.isconnected():
                pass
            print('network config:', sta_if.ifconfig())
            self.ip_info = sta_if.ifconfig()
            
    def get_ip_info(self):
        return self.ip_info
        
    def Update(self):
        suppress = True