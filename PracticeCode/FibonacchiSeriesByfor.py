def getFibo(n):
    first=0
    second=1
    third=0
    for i in range(1,n+1):
        print(third)
        third=first+second
        first=second
        second=third
def call():
    try:
        n=int(input("Enter number"))
        getFibo(n)
    except ValueError as a:
        print("Invalid value",a)
call()