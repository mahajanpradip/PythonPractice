def GetFibo(number):
    a=0
    b=1
    c=0
    print(c)
    c=a+b
    while(c<=number):
        print(c)
        c=a+b
        a=b
        b=c
def call():
    try:
        number=int(input("Enter number"))
        GetFibo(number)
    except ValueError as a:
        print(a,"Invalid value")
call()