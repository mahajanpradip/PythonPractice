def getSum(number):
    sum=0
    i=1
    while i<=number:
        sum=sum+i
        i+=1
    return sum
def printSum():
    try:
        number=int(input("Enter number till you want sum"))
        num= getSum(number)
        print(num)
    except ValueError as v:
        print("Invalid value",v)
printSum()