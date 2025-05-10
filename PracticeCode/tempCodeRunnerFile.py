def getPrimeNumbers(i,number):
    count=0
    while i<=number:
        count=0
        j=i
        while j<=number:
            if i % j==0:
               count+=1
               j+=1 
        if count==2:
            print(i)
        i+=1
def calling():
    try:
        start=int(input("Enter starting number"))
        num=int(input("Enter ending number"))
        getPrimeNumbers(start,num)
    except ValueError as v:
        print("Invalid input")
calling()