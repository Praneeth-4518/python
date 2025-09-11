from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class rectangle(shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print(f"area of rec:{self.length*self.breadth}") 
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print(f"area of circle:{3.14*self.radius*self.radius}")
rec=rectangle(45,18)
rec.area()
cir=circle(7)
cir.area()                
