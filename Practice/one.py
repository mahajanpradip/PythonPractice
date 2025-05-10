class one:
    def __init__(self,name):
        self.name=name
        
    def funct(self):
        print(f"name :{self.name}")
        
class two(one):
    def pp(self):
        usern=input("Enter name")
        obj=two(usern)
        obj.funct()

t=two("Pradip Mahjan")
t.pp()
