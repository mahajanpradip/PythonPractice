class CustomException(Exception):
    pass

class Voting:
    def check(self,age):
        if age <18:
            raise CustomException("Not eliglible for vote")
        else:
            print("Voting allowed")
def call():
    try:
        obj=Voting()
        age=int(input("Enter age"))
        obj.check(age)
    except ValueError as v :
        print("Invalid input")
    except CustomException as c:
        print("Voter must be 18+")
call()