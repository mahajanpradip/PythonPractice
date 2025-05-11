class Animals:
    def __init__(self,name):
        self.name=name
        
    def speak(self):
        print(f"{self.name} is makes a sound")
    def run(self):
        print(f"{self.name} is running")
class Dog(Animals):
    def __init__(self,name):
        super().__init__(name)
    def speak(self):
        return super().speak()
    def run(self):
        return super().run()
dog = Dog("bull dog")
dog.speak()
dog.run()