def checkPrime(number):
    isprime=True
    i=2
    while i<number:
        if number % i ==0:
            isprime=False
            break
        i+=1
    return isprime
def calling():
    try:
        prime=int(input("Enter number"))
        result= checkPrime(prime)
        if(result):
            print("prime ")
        else:
            print("not prime")
    except ValueError as e:
        print("Invalid Value",e)
calling()
        