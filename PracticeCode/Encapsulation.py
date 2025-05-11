class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=object
        self.__balance=balance  #private variable
    def deposite(self,amount):
        if amount > 0 :
            self.__balance+=amount
            print(f"Deposite {amount}.new balance {self.__balance}")
        else:
            print("Enter valid amount for deposite")
    def withdraw(self,amount):
        if amount > 0 and amount <=self.__balance:
            self.__balance-=amount
            print(f"withdraw {amount} . current balance {self.__balance}")
        else:
            print("Withdraw faild")
    def CurrentBalance(self):
        return self.__balance
accunt=BankAccount("Pradip",500)
accunt.deposite(2000)
accunt.withdraw(500)
print("current balance ",accunt.CurrentBalance())
        