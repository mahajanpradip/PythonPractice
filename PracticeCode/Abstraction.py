from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def Draw(self):
        pass
class circle(shape):
    def Draw(self):
        print("Drawing circle")
class Rectangle(shape):
    def Draw(self):
        print("Drawing Rectangle")
c=circle()
c.Draw()
r=Rectangle()
r.Draw()