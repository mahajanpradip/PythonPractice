def checkGerator(num1,num2):
    if num1>num2:
        print("Number first is Greator than : ",num1 ,">", num2)
    else:
        print("Number second is Greator than : ",num2 ,">",num1)
def calling():
    try:
        num1=int(input("Enter first number  :  "))
        num2=int(input("Enter second number :  "))
        checkGerator(num1,num2)
    except ValueError as v:
        print("Invalid value")
calling()