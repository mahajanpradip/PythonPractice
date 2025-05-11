class Number:
    def CheckPerfectNumber(self,num):
        sum=0
        division=[]
        for i in range(1,num):
            if(num%i==0):
                division.append(i)
        for i in division:
            sum=sum+i
        return sum
class Calling(Number):
    @staticmethod
    def call():
        try:
             number=int(input("Enter number"))
             obj=Calling()
             result = obj.CheckPerfectNumber(number)
             if result is not None:
                    if result==number:
                        print("Its a Perfect number")
                    else:
                         print("This is not perfect number")
        except ValueError as e:
            print("Invalid input",e)
Calling.call()