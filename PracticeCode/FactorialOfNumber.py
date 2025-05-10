def GetFactorial(n):
    factorial=1
    for i in range(1,n+1):
        factorial=factorial*i
    return factorial
def call():
    try:
        number=int(input("Enter number"))
        result=GetFactorial(number)
        print(result)
    except ValueError as a:
        print("Invalid Input : ",a)
call()