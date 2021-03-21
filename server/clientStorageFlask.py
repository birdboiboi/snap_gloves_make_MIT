import socket
import threading 
import sys
import Text_feature
from clientStorage import ClientStorage

class ClientStorageFlask (ClientStorage):
    def __init__(self,socket_server,address,connection,bytes_to_recv = 1024):
        super(ClientStorageFlask,self).__init__(socket_server,address,connection,bytes_to_recv = 1024)
        self.socket_server = socket_server
        self.address = address
        self.connection = connection
        self.bytes_to_recv = bytes_to_recv
        print("start server")
        self.headers_dict = {"GLOVE":self.set_id_glove,
                                "":self.pass_this,
                                "CMD_IOT":self.IOT_CMD,
                                "CMD_ROBOT":self.ROBOT_CMD}
        #self.send_msg()
    def IOT_CMD(self,CMD):
        self.message = CMD
        Text_feature.run()
        pass