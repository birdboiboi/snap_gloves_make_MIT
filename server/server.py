import socket
from threading import Thread
import clientStorage
import sys

sys.stdout.flush()

class Server():
    kill = False
    client_list = []
    
    def __init__(self,ip_add = '10.0.0.64',port = 8080):
        self.ip_add = ip_add
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((ip_add, port))
        self.s.listen(5)
        self.cmd_dict = {"KILL":self.kill_all,"":self.pass_this,"LIST":self.list_all}
        #self.s.bind((self.ip_add,self.port))
        print("server init")
        
    def run(self):
        t = Thread(target =self.check_input)
        t2 = Thread(target = self.handle_server)
        t2.daemon = True
        t.start()
        t2.start()
        print("run")
        
            
            
        #t.join()
        t2.join()
        
    def handle_server(self):
        while not self.kill:
            print("accepting")

            c,addr = self.s.accept()
            sys.stdout.flush()
            idx = self.check_client_list(addr)

            #sys.stdout.flush()
            if idx != -1:                           #address,connection
                print("--existing--")
                self.client_list[idx].set_add_connect(addr,c)
                print("existing")
            else:
                print("--new--")                                                   #socket_server,address,connection
                self.client_list.append(clientStorage.ClientStorage(self.s,addr,c))    
                print(self.client_list)        
                self.client_list[idx].send_msg("200 OK")
                #self.client_list[idx].send_msg("stupid follow up")
                self.client_list[idx].on_connect()
            
        self.s.close()
        
    def check_client_list(self,addr):
        for client in self.client_list:
            print("this",addr)
            print("in class client",client.address)
            if client.address[0] == addr[0]:
                return self.client_list.index(client)
        return -1
        
    def check_input(self):
        #global self.client_list

        while not self.kill:
            
            sys.stdout.flush()
            cmd = input("input cmd: ")
            if cmd == None:
                cmd = ""
            self.cmd_dict[cmd.upper()]()
            print(len(self.client_list),"clients connected")
        
    def kill_all(self):
        print(self.client_list)
        self.kill = True
        for client in self.client_list:
            client.sustain =False
        print ("connect again to kill process")
        
    def pass_this(self):
        pass
        
    def list_all(self):
        print( self.client_list)
        for client in self.client_list:
            print("machine name",client.mac_id,"msg",client.message)
ser = Server(ip_add = "192.168.68.141",port = 8080)
ser.run()
