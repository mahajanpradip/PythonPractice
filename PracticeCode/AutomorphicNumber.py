def checkAutomorphicNumber():
    try:
        number = int(input("Enter number"))
        if(number>=0):
            def getSquare(number):
                return number * number
            result=getSquare(number)
            square=str(number)
            n=str(result)
            return n.endswith(square)
        else:
            print("Plese enter non negative number")
            return False
    except ValueError as v:
        print("Invalid Input")
        return False
n=checkAutomorphicNumber()
if n:
    print("Automorpgic number")
else:
    print("Not automorphic number")
    