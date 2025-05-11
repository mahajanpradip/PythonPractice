def CheckHarshadNumber():
    try:
        num = int(input("Enter Number"))
        if num <=0:
            return False
        sum=0
        temp=num
        rem=0
        while temp>0:
            rem=temp%10
            sum=sum+rem
            temp//=10
        if num % sum==0:
            return True
        else:
            return False
    except ValueError as v:
           print("Enter valid input",v)
           return False
sum=CheckHarshadNumber()
if sum:
    print("This is Harshad number")
else:
    print("Not Harshad Number")