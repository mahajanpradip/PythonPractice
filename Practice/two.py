class demo:
    def __init__(self):
        self.name="Pradip"
        
    def __init__(self,name):
        self.name=name
    
    def prt(self):
        print(f"name: {self.name}")
class temp(demo):
    def ok(self):
        user=input("Eneter name")
        obj =temp(user)
        obj.prt()
t=temp("This is name")
t.ok()