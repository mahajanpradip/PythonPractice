class Network:
    def __init__(self,name,number):
        self.name=name
        self.number=number
    def Generation(self):
        print(f"{self.name} of generation {self.number}")
    def features(self):
        print(f"{self.name} features are :is basic network : voice call inable")
class idea(Network):
    def __init__(self, name, number):
        super().__init__(name, number)
    def Generation(self):
        print(f"{self.name} of generation {self.number} ")
    def features(self):
        print(f"{self.name} features are : internate and sms service")
class jio(idea):
    def __init__(self, name, number):
        super().__init__(name, number)
    def Generation(self):
        print(f"{self.name} is of generation {self.number}")
    def features(self):
        print(f"{self.name} features are : free calls")
obj=Network("simple",1)
obj.Generation()
obj.features()
obj2=idea("idea",2)
obj2.Generation()
obj2.features()
obj3=jio("jio",3)
obj3.Generation()
obj3.features()
