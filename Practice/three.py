class one:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def prt(self):
        print(f"name : {self.name},age :{self.age}")
    
class two(one):
    def func(self):
        usern=input("Enter name")
        usera=int(input("Enter age"))
        obj=two(usern,usera)
        obj.prt()
t=two("ok",23)
t.func()