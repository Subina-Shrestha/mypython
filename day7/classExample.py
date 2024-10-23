class account:
    def __init__(self,accno,name,balance,accType):#init is used to define constrctor
        self.accno=accno
        self.name=name
        self.balance=balance
        self.accType=accType

    def printDetails(self):
        print(f"account number:{self.accno}, name:{self.name}, balance:{self.balance},account type={self.accType}")
    def getBalance(self):
        return self.balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if(self.balance<amount) or (self.accType=="fixed"):
            return False
        
        self.balance-=amount
        return True
al=account(43,"subina",34000.04,"savings")
al.printDetails()
al.withdraw(3400)
al.printDetails()
if not al.withdraw(3400):
    print(f"acount{al.accno} cannot b withdrawn") 


