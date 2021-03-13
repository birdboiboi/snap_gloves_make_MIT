import classHandler
class sampleClass(classHandler.ClassHandler):
    def Start(self):
        print(self.__str__(), "instantiated")
        print("sampleClass Start")
        
    def Update(self):
        print(self.__str__(), "instantiated")
        print("sampleClass Update")