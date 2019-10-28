class BankAccount:
    def _init_(self):
        self.accountNumber=int(input("Enter the account number:"))
        self.balance=int(input("Enter the amount:"))
  
def withdrawl(self):
    amo=int(input("Enter the amount:"))
if amo<self.balance:
    print("you cannot withraw due to insufficient balance")
else:
    self.balance=self.balance-amo
    print("you withdrew ",amo)
    print("\n Available balance ",self.balance,"$")
  
def deposit(self):
    amo=int(input("Enter the amount:"))
    self.balance=self.balance+amo
    print("Amount deposited ",amo)
print("\n Available balance ",self.balance,"$")
  
def getBalace(self):
    print("\n Available balance ",self.balance,"$")
  
class CheckingAccount(BankAccount):
    def deductFees(self,fees=5):
        self.fees=fees
        if self.fees<=self.balance:
            self.balance=self.balance-5
            print("Fees deducted $5 \n")
            print("\n Available balance ",self.balance,"$")
        else:
            print("\n Fees can't be deducted due to insufficient balance")
  
def checkMinimumBalance(self,minimumBalance=50):
    self.minimumBalance=minimumBalance
    if self.balance>self.minimumBalance:
        print("\n There is enough balance in your account")
        print("\n Available balance ",self.balance,"$")
    else:
       print("\n There is no minimum balance in your account")
       print("\n Minimum balance is 50$")

class SavingAccount(BankAccount):
    def addInterest(self,interestRate=2):
        self.interestRate=interestRate
        interestamo=(self.balance*self.interestRate)/100;
        self.balance=self.balance+interestamo;
        s= CheckingAccount()
while(1):
    print("------------------------------------------------------------------\n")
    print(" 1.Enter account information\n 2.Withdraw money\n 3.Deposit money\n\
    4.Know Balance\n 5.Deduct fees\n 6.Check minimum balance\n\
    7.Add interest\n 8.Exit")
    ch=int(input("Enter the choice:"))

if(ch==1):
    s._init_()
elif(ch==2):
        s.withdrawl()
elif(ch==3):
        s.deposit()
elif(ch==4):
        s.getBalace()
elif(ch==5):
        s.deductFees()
elif(ch==6):
        s.checkMinimumBalance()
elif(ch==7):
        s.addInterest()
elif(ch==8):
        exit(0)
else:
    print("Invalid choice")