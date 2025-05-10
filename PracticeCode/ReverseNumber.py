def ReverseNumber(number):
    if number < 0:
        return
    if number == 0 :
        return
    rem=0
    reversenum=0
    while(number>0):
        rem=number%10
        reversenum=rem+reversenum*10
        number=number//10
    return reversenum
def call():
    try:
        num=int(input("Enter number"))
        rev=ReverseNumber(num)
        if rev is not None:
            print(rev)
    except ValueError as v:
        print("Invalid Input")
call()