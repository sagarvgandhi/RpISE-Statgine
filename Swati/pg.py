class piggybank:
    def __init__(self):
        self.balance=0
        self.lt=0
        self.transaction=[]
    def deposit(self,amount):
        self.balance=self.balance+amount
        self.lt=amount
        self.transaction.append(self.lt)
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance=self.balance -amount
            self.lt= -amount
            self.transaction.append(self.lt)
    def statement(self):
        print('the balance is', self.balance)
        print('last transaction is', self.lt)
        print(self.transaction)
        print(self.transaction[-10:-1])
        

pg1= piggybank()


print('welcome tp piggy bank')
action= input('desired action',)
while action!='q':
    if action =='d':
        v=int(input('the value to deposit is'))
        pg1.deposit(v)
    if action== 'w':
        v=int(input('the value to withdraw is'))
        pg1.withdraw(v)
    if action== 's':
        pg1.statement()
    action= input('desired action',)
print('thank you ')
