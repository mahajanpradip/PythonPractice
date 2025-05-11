class Number:
    def CheckStrongNumber(self,number):
        temp=number
        rem,sum,digit=0,0,1
        while(temp>0):
            rem=temp%10
            digit=1
            for i in range(1,rem+1):
                digit=digit*i
            sum=sum+digit
            temp//=10
        return sum
class Checker(Number):
    def call(self):
        try:
            number=int(input("Enter number"))
            result=self.CheckStrongNumber(number)
            if result is not None:
                if(result==number):
                     print("This is Strong Number : ",result)
                else:
                      print("Not  a strong Number : ",result)
        except ValueError as v:
                print("Invalid Input")
    @classmethod
    def calling(cal):
        cal=cal()
        cal.call()
Checker.calling()              
    
                