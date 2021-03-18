From machine import SPI
From samplePinRead import SamplePinRead

class SPI_MOD(SamplePinRead):
    def __init__(self,name = "no name",
                 pin_out =[],
                 pin_in=[],
                 pull_up=[],
                 pull_down=[],
                 baudrate=115200,
                 bits=8 ):
        super(SPIHandler,self).__init__(name,pin_out,pin_in,pull_up,pull_down)
        self.spi_object = SPI(baudrate=115200,bits=8 )
        

def Start(self):
        self.Setup_Pins_Out()
        self.Setup_Pins_In()

def Set_Up_SPI():
    self.spi_object.MSB =self.pin_mac_in[1]
    self.spi_object.mosi=self.pin_mac_out[0]#sdo
    self.spi_object.miso =self.pin_mac_in[0]#sdi
    self.spi_object.sck =self.pin_mac_in[1]
