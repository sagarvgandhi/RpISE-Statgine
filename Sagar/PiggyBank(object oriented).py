print("\t\tWelocme to OO Piggy Bank\t\t")
print("\nEnter Which Piggy Bank You Want To Use: 1 or 2")
read=int(input())
print("\nPlease Select From The Below Options: ")

class PiggyBank:
    """docstring for PiggyBank."""
    def __init__(self):
            self.balance = 0
            self.lt=0
            self.transaction=[]
    def deposit(self, amount):
        self.balance=self.balance+amount
        self.last_transaction=amount
        self.transaction.append(self.last_transaction)
        print("\nLast Transaction: ",self.last_transaction,"Cr")
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance=self.balance-amount
            self.last_transaction=amount
            self.transaction.append(self.last_transaction)
            print("\nLast Transaction: ",self.last_transaction,"Dr")
        else:
            print("\nYou don't have enough balance to withdraw")
    def statement(self):
        print("\nCurrent Balance: ",self.balance)
        print("Last Transaction: ",self.last_transaction)
    def last_fewtransaction(self):
        x=int(len(self.transaction))-1
        for i in self.transaction:
            print("Last Transactions: ",self.transaction[x])
            x = x - 1
    def quit(self):
        print("Good Bye")

def userfunction(l):
    user_option=0
    while user_option!=5:
         print("\nYour Options are : \n1-Deposit \n2-Withdraw \n3-Statement \n4-Last 10 Transaction \n5-Quit")
         user_option=int(input("\nPlease Enter an Option: "))
         if (user_option==1):
            Value_deposit=int(input("\nPlease Enter value to Deposit: "))
            l.deposit(Value_deposit)
            l.statement()
         elif (user_option==2):
            Value_withdraw=int(input("\nPlease Enter value to Withdraw: "))
            l.withdraw(Value_withdraw)
            l.statement()
         elif (user_option==3):l.statement()
         elif (user_option==4):l.last_fewtransaction()
         elif (user_option==5):l.quit()
         else:
            print("You have entered invalid option")

if (read==1):
    pg1=PiggyBank()
    userfunction(pg1)
else:
    pg2=PiggyBank()
    userfunction(pg2)
