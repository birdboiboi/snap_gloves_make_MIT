import classHandler
import SampleClass 
import samplePinRead
import networkHandler
import clientHandler
from multiI2cHandler import I2c_MOD_Multi
from unitTestNetworkHandler import UnitTestNetworkHandler

def get_list_of_imports():
    #include all scripts like 
    NH = networkHandler.NetworkHandler(wifi_name = "******",password = "*******")
    CH = clientHandler.ClientHandler(name = "client",
                                    network_handler = NH,
                                    server_ip = "192.168.68.141",
                                    port = 8080),

    ls = [NH,
          UnitTestNetworkHandler(name = "client",
                                    network_handler = NH,
                                    server_ip = "192.168.68.141",
                                    port = 8080),
          I2c_MOD_Multi(name = "Multi",pin_in = [16,16,16],
                        pin_out= [17,18,17,19,17,23],
                        pull_up= [18,19,23],
                       pass_names = ["arm","pointer","middle","ring","pink","thumb"],CH = CH)
            
        ]
    return ls
