def checkYear(year):
    if (year % 2 == 0 and year % 100 != 0) or (year%400==0):
        print("This is leep year : ",year)
    else:
        print("Not leap year : ",year)
def calling():
    try:
        year=int(input("Enter year :=> "))
        checkYear(year)
    except ValueError as e:
        print("Invalid value")
calling()
