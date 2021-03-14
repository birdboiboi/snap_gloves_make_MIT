import classHandler
import SampleClass 
import samplePinRead
import networkHandler

def get_list_of_imports():
    #include all scripts like 
    #samplePinRead.SamplePinRead(name = "pinRead1",pin_out = [0,2],pin_in = [5,12,4],pull_down = [5,4]),
    ls = [networkHandler.NetworkHandler(wifi_name = "SSID",password = "password"),
          samplePinRead.SamplePinRead(name = "pinRead1",pin_out = [0,2],pin_in = [5,12,4],pull_down = [5,4]),
        ]
    return ls
