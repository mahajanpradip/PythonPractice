name=input("Enter string for check")
def reverse(s):
    revers=""
    for char in s:
        revers=char+revers
    return revers
if reverse(name)==name:
    print("This is pelindrome")
else:
    print("This is not pelindrome")