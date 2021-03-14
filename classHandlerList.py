import classHandler
import SampleClass 
import samplePinRead


def get_list_of_imports():
    ls = [samplePinRead.SamplePinRead(name = "pinRead1",pin_out = [0,2],pin_in = [5,12,4],pull_down = [5,4]),
        ]
    return ls
