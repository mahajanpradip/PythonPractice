def checkEvenOrOdd(number):
    if number % 2==0:
        print("Even Number : ",number)
    else:
        print("Odd number : ",number)
def cllaing():
    try:
        number =int(input("Enter number"))
        checkEvenOrOdd(number)
    except ValueError as e:
        print("Invalid value",e)
cllaing()