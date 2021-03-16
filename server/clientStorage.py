import socket
from threading import Thread

class ClientStorage():

    #https://stackoverflow.com/questions/10810249/python-socket-multiple-clients
    message = ""
    message_to_send  = "connected"
    sustain = True
    run_state = False
    t_this = None
    
    def __init__(self,socket_server,address,connection,bytes_to_recv = 1024):
        self.socket_server = socket_server
        self.address = address
        self.connection = connection
        self.bytes_to_recv = bytes_to_recv
        #self.send_msg()
        
    def set_add_conect(self,address,connection):
        self.address = address
        self.connection = connection
        
    def send_msg(self,msg = None):
        #try:
        print(self.connection)
        
        if msg == None:
            print("sending",msg, " as", msg.encode('utf-8'))
            self.connection.send(self.message_to_send.encode('utf-8') )
        else:
            print("sending",self.message_to_send, " as", self.message_to_send.encode('utf-8'))
            self.connection.send(msg.encode('utf-8') )
        #except:
            #self.error()
        print("recv fail")

    def recv_msg(self):
        
        #try:
        while self.sustain:
            data = self.connection.recv(self.bytes_to_recv).decode('utf-8')
            if len(data)>0:
                self.message = data
                print("msg" +self.message)
                
        self.connection.close() 
        #except:
        print("recv fail")
            #self.error()
        #self.t_this.join()
            
    def run(self):
        print("****************")
        if not self.run_state:
            self.run_state = True
            #self.t_this = Thread(self.recv_msg())
            self.recv_msg()
            self.t_this.start()
        
    def error(self):
        print(self.connection,self.address," not able to send ")
        self.sustain = False
        #self.t_this.join()
        pass