def GetPower(n,power):
    result=1
    for _ in range(n+1):
        result=result*n
    return result
def call():
    try:
        number=int(input("Enter Number"))
        power=int(input("Enter power "))
        pow=GetPower(number,power)
        print(pow)
    except ValueError as v:
        print("Invalid Input ",v)
call()