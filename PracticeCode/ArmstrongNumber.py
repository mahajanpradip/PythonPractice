def checkArmStrongNumber(number):
    temp=number
    count=0
    while temp > 0 :
        temp//=10
        count+=1
    temp=number
    rem=0
    sum=0
    while(temp>0):
        rem=temp%10
        digit=1
        for i in range(1,count+1):
            digit=digit*rem
        sum=sum+digit
        temp//=10
    return sum
def call():
    try:
        number=int(input("Enter number "))
        result=checkArmStrongNumber(number)
        if result is not None:
            if(result==number):
                print("Armstrong : ",result)
            else:
                print("Not Armstrong")
        else:
            print("Invalid ")
    except ValueError as v:
        print("Invalid Input")
call()