def GetPrimeFactor(n):
    for i in range(1,n+1):
        count=0
        for j in range(1,i+1):
            if(i%j==0):
                count+=1
        if(count==2):
            if(n%i==0):
                print(i)
def call():
    try:
        number=int(input("Enter Number"))
        GetPrimeFactor(number)
    except ValueError as v:
        print("Invalid Input")
call()