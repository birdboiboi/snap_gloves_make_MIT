import clientHandler

import classHandler
import networkHandler as NH
import socket
import _thread

class UnitTestNetworkHandler(clientHandler.ClientHandler):

    def __init__(self,name = None,network_handler = None,server_ip = None,port = None):
        super(UnitTestNetworkHandler, self).__init__(name,network_handler,server_ip,port)
        
    def Update(self):
        self.write(self,"are you listening?")
        