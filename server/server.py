
import socket
from threading import Thread
import clientStorage

class Server():
    kill = False
    client_list = []
    def __init__(self,ip_add = '10.0.0.64',port = 8080):
        self.ip_add = ip_add
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((ip_add, port))
        self.s.listen(5)
        #self.s.bind((self.ip_add,self.port))
        
    def run(self):
        while not self.kill:
            c = self.s.accept()[0]
            addr= self.s.accept()[1]
            print("c",c)
            print ("addr",addr)
            idx = self.check_client_list(addr)
            if idx != -1:                           #address,connection
                self.client_list[idx].set_add_connect(addr,c)
            else:
                                                                    #socket_server,address,connection
                self.client_list.append(clientStorage.ClientStorage(self.s,addr,c))
            self.client_list[idx].send_msg("200 OK")
            self.client_list[idx].run()
        self.s.close()
        
    def check_client_list(self,addr):
        for client in self.client_list:
            if client == addr:
                return self.client_list.index(client)
        return -1
        
ser = Server(ip_add = "10.0.0.64",port = 8080)
ser.run()