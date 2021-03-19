import socket
import threading 
import sys

class ClientStorage():

    #https://stackoverflow.com/questions/10810249/python-socket-multiple-clients
    message = ""
    message_to_send  = "connected"
    sustain = True
    run_state = False
    t_this = None
    mac_id = ""
    
    
    def __init__(self,socket_server,address,connection,bytes_to_recv = 1024):
        self.socket_server = socket_server
        self.address = address
        self.connection = connection
        self.bytes_to_recv = bytes_to_recv
        print("start server")
        self.headers_dict = {"GLOVE":self.set_id_glove,"":self.pass_this}
        #self.send_msg()
        
    def set_add_connect(self,address,connection):
        self.address = address
        self.connection = connection
        print("set_add_connect")
        
    def send_msg(self,msg = None):
        #try:
        #print("connect",self.connection)
        
        if msg == None:
            print("sending",self.message_to_send, " as", self.message_to_send.encode('utf-8'))
            self.connection.send(self.message_to_send.encode('utf-8') )
        else:
            print("sending",msg, " as", msg.encode('utf-8'))
            self.connection.send(msg.encode('utf-8') )
        #except:
            #self.error()
        print("recv fail")

    def recv_msg(self):
        #while self.sustain:
        #try:
        print("recv")
        sys.stdout.flush()
        data = self.connection.recv(self.bytes_to_recv).decode('utf-8')
        
        if len(data)>0:
            self.message = data
            self.process_data(self.message)
            print("msg" +self.message)
                
         
        #except:
        print("message recved")
            #self.error()
        #self.t_this.join()
        
    def on_connect(self):
        #while self.sustain:
        sys.stdout.flush()
        self.send_msg("bird")
        self.t_this = threading.Thread(target = self.recv_msg)
            #threading.threads.append(t_this)
        self.t_this.start()
        self.t_this.join()
        self.connection.close() 
        
    def process_data(self,string_to_process):
        print("process_data",string_to_process)
        string_to_process = string_to_process.split(":")
        print(string_to_process[1])
        self.headers_dict[string_to_process[0]](string_to_process[1])
        
    def set_id_glove(self,id_given):
        print("init glove",id_given)
        self.mac_id = id_given
        print(self.mac_id)
        
        
    def pass_this(self):
        pass   
        
    def run(self):
        print("****************")
        if not self.run_state:
            self.run_state = True
            #self.t_this = threading.Thread(self.recv_msg())
            self.on_connect()
            #self.t_this.start()

    def error(self):
        print(self.connection,self.address," not able to send ")
        self.sustain = False
        #self.t_this.join()
        pass