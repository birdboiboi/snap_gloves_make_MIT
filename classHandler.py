class ClassHandler():
    suppress = False
    suppress_print = False
    def __init__(self,name="no name"):
        self.name = name
        
    def Start(self):
        print(self.__str__(), "instantiated")
    def Update(self):
        print(self.__str__(), "instantiated")
    def isTypeCH():
        return True
    def __str__(self):
        if not self.suppress_print:
            return("class type ",self.__class__.__name__," inst name ",self.name)
        