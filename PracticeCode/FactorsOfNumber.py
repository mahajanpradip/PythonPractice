def GetFactors(n):
    for i in range(1,n+1):
        if(n%i==0):
            print(i)
def call():
    try:
        number=int(input("Enter number"))
        GetFactors(number)
    except ValueError as v:
        print("Invali input",v)
call()