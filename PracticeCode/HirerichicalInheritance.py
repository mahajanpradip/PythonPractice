class simcards:
    def simInfo(self):
        print("Supports calling and internate")
class vi(simcards):
    def vifeature(self):
        print("Vi : has high cost plans and  dicent coverage")
class jio(simcards):
    def jioFeatures(self):
        print("jio : 4G strong network and free callings")
class Airtel(simcards):
    def AirtelFeatures(self):
        print("Airtel : has good network ")
obj1=jio()
obj1.simInfo()
obj1.jioFeatures()
print("--------------------------------------------")
obj2=vi()
obj2.simInfo()
obj2.vifeature()
print("--------------------------------------------")
obj3=Airtel()
obj3.simInfo()
obj3.AirtelFeatures()
