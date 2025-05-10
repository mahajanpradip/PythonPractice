def getSumOdDigitOfGivenNumber(number):
    if(number<=0):
        print("invalid number")
        return
    rem=0
    sum=0
    while number >0 :
        rem=number%10
        sum=sum+rem
        number=number/10
    return sum
def call():
    try:
        number=int(input("Enter number"))
        result=getSumOdDigitOfGivenNumber(number)
        if result is not None:
            print("Sum of the digit of given number is  :=> ",int(result))
    except ValueError as a:
        print("Invalid input",a)
call()
        