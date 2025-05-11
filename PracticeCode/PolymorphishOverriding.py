class Animal:
    def walk(self):
        print("Animal is walking")
class Dog(Animal):
    def walk(self):
        print("Dog is walking")
class Cat(Animal):
    def walk(self):
        print("cat is walking")
obj=[Animal(),Dog(),Cat()]
for ob in obj:
    ob.walk()