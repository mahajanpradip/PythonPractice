num=int(input("Enter number"))
def arm(num):
    temp=num
    temt=num
    rem=0
    summ=0
    count=0
    while temp>0:
        temp=temp//10
        count+=1
    while temt>0:
        rem=temt%10
        i=1
        summ=summ+rem**count
        temt=temt//10
    return summ
s=arm(num)
if s==num:
    print("armstrong number",num)
else:
    print("not armstrong",num)
            
            
            