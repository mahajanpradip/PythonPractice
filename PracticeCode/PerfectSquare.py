import math
def GetPerfectSquare(number):
    return number*number
def Call():
    try:
        n=int(input("Enter number"))
        result = GetPerfectSquare(n)
        if result is not None:
           squrt=math.isqrt(n)
           if squrt * squrt == n:
               print(f"{n}  Its a perfect square, the square root of number is{squrt}")
               print(f"This perfect square of {n} is {result}")
           else:
               print("This is not perfect square")
        
    except ValueError as v:
        print("Invalid Input ",v)
Call()