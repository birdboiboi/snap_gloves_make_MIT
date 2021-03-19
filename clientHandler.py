import classHandler
import networkHandler as NH
import socket
import _thread

class ClientHandler(classHandler.ClassHandler):
    #https://docs.micropython.org/en/latest/esp8266/tutorial/network_tcp.html
    #network_handler = NH.NetworkHandler()
    message_recv = ""
    message_to_send = "GLOVE:empty"
    #network_handler
    has_tcp = False
    sustain = True
    
    def __init__(self,name = None,network_handler = None,server_ip = None,port = None):
        super(ClientHandler, self).__init__()
        print(name,server_ip,port)
        self.addr_info = socket.getaddrinfo(server_ip,port)
        self.network_handler = network_handler
        print (self.network_handler.get_ip_info())
        
    def Start(self):
        print(self.name,"starting client tcp send")
        self.message_to_send = "GLOVE:"+str(self.name)
        self.establish_tcp()
        #try:
        
        print(self.message_to_send)
        self.write()
        #except:
        print("send success")
          
    def establish_tcp(self):
        self.sock = socket.socket()
        print("attempting connecting to ",self.addr_info) 
        self.sock.connect(self.addr_info[0][-1])
        _thread.start_new_thread(self.listen())
        
        print("no tcp connection made on", self.addr_info[0][-1])
    
    def write(self,message_to_send= None):
        print("attempting to send ",message_to_send," to " , self.addr_info) 
        if self.has_tcp:
            if message_to_send != None:
                self.sock.send(message_to_send)
            else:
                self.sock.send(self.message_to_send)
        
    def listen(self):
        self.has_tcp = True
        self.write()
        while self.sustain:
            data_in = self.sock.recv(500)
            if len(data_in)>0:
                self.message_recv = data_in
                print("message",self.message_recv)
            
    def Update(self):
        suppress = True