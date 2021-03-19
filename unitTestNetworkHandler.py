import clientHandler

import classHandler
import networkHandler as NH
import socket
import _thread

class UnitTestNetworkHandler(clientHandler.ClientHandler):

    def __init__(self,name = None,network_handler = None,server_ip = None,port = None):
        super(UnitTestNetworkHandler, self).__init__(name,network_handler,server_ip,port)
        self.sustain = False
        
    def Update(self):
        print("ask")
        self.post("CMD_IOT:GOOGLE_THIS")
        self.post("CMD_ROBOT:ROBOT")
        self.sustain = False