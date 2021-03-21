import classHandler
import SampleClass 
import samplePinRead
import networkHandler
import clientHandler
from multiI2cHandler import I2c_MOD_Multi
from unitTestNetworkHandler import UnitTestNetworkHandler

def get_list_of_imports():
    #include all scripts like 
    #samplePinRead.SamplePinRead(name = "pinRead1",pin_out = [0,2],pin_in = [5,12,4],pull_down = [5,4]),
    NH = networkHandler.NetworkHandler(wifi_name = "50RiverRd",password = "Herc51000")
    ls = [NH,
          #samplePinRead.SamplePinRead(name = "pinRead1",pin_out = [0,2],pin_in = [5,12,4],pull_down = [5,4]),
          #clientHandler.ClientHandler(name = "client",network_handler = NH,server_ip = "192.168.68.141",port = 8080),
          UnitTestNetworkHandler(name = "clientUnit",network_handler = NH,server_ip = "192.168.68.141",port = 8080),
                                                   #pin_in = [sda],pin_out=[scl,ad0]
          #I2c_MOD_Multi(name = "Multi",pin_in = [16],pin_out= [17,18],pull_up= [18,19,23],pass_names = ["arm","pointer","middle"])

        ]
    return ls
