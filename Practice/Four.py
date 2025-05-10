from abc import ABC,abstractmethod

class Animal:
    @abstractmethod
    def walk(self):
        pass
    @abstractmethod
    def eat(self):
        pass
class dog(Animal):
    def walk(self):
        print("dog is walking")
    def eat(self):
        print("dog is eating")
class Tiger(Animal):
    def walk(self):
        print("tiger is walking")
    def eat(self):
        print("Tiger is eating")
        
class main:
   def __init__(self):
        obj1=dog()
        obj1.walk()
        obj1.eat()
        obj2=Tiger()
        obj2.walk()
        obj2.eat()
    obj=main()