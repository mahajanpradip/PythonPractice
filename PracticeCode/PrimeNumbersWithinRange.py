def checkPrime(start,end):
    for i in range (start,end+1):
        if i>1:
            count=0
            for j in range (1,i+1):
                if i % j==0:
                    count+=1
            if(count==2):
                print(i)
def calling():
    try:
        start=int(input("Enter starting number"))
        end = int(input("Enter ending number"))
        checkPrime(start,end)
    except ValueError as v:
        print("Invalid value")
calling()