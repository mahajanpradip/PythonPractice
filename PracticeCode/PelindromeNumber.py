def CheckPelindromeNumber(Number):
    if Number <=0:
        print("Invalid ")
        return
    rem=0
    reverseN=0
    while Number >0:
        rem=Number%10
        reverseN=rem+reverseN*10
        Number=Number//10
    return reverseN
def call():
    try:
        num=int(input("Enter number"))
        rev=CheckPelindromeNumber(num)
        if rev is not None :
            if rev==num:
                print("Number is pelindrome : ",num," :: ",rev)
            else:
                print("Not Pelindrome : ",num," :: ",rev)
    except ValueError as v:
            print("Invalid Input")
call()
        