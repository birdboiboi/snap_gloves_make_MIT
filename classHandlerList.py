import classHandler
import SampleClass 
import samplePinRead
import networkHandler
import clientHandler
from unitTestNetworkHandler import UnitTestNetworkHandler

def get_list_of_imports():
    #include all scripts like 
    #samplePinRead.SamplePinRead(name = "pinRead1",pin_out = [0,2],pin_in = [5,12,4],pull_down = [5,4]),
    NH = networkHandler.NetworkHandler(wifi_name = "House Stark",password = "We@rebroke123")
    ls = [NH,
          #samplePinRead.SamplePinRead(name = "pinRead1",pin_out = [0,2],pin_in = [5,12,4],pull_down = [5,4]),
          #clientHandler.ClientHandler(name = "client",network_handler = NH,server_ip = "10.0.0.64",port = 8080),
          UnitTestNetworkHandler(name = "clientUnit",network_handler = NH,server_ip = "10.0.0.64",port = 8080)

        ]
    return ls
