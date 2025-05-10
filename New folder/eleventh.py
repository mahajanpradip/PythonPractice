num=int(input("Take a number"))
def check(num):
    rem=0
    s=0
    while num>0:
        rem=num%10
        s=rem+s*10
        num=num//10
    return s
nn=check(num)
if nn==num:
    print("is pelindrome")
else:
    print("not pelindrome")