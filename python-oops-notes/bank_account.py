class BankAccount:
    def __init__(self, accountNumber, accountName,ifseCode,balance=0):
        self.accountNumber = accountNumber
        self.accountName = accountName
        self.ifseCode = ifseCode
        self.balance = balance
    def deposit(self,ammount):
        self.balance+=ammount
    def withdraw(self,ammount):
        self.balance-=ammount
    def checkBalance(self):
        print(self.balance)

#this is where u play with the code like you played in maze game left(), right(), move() 
account1 = BankAccount("1234567890", "John Doe", "1234567890", 1000)
account2 = BankAccount("1234567891", "Jane Doe", "1234567891", 2000)
# can give number of accounts
account1.checkBalance()
account2.checkBalance()
#checking balence
#depositing money to account1, checking balence, withdrawing money from account1, checking balence
account1.deposit(100)
account1.checkBalance()
account1.withdraw(500)
account1.checkBalance()

# this is a comment
""" When you write:account1 = BankAccount("123", "John", "IFSC001", 1000)
Python does this behind the scenes:
- Creates a new object in memory (let’s call it obj1)
- Calls BankAccount.__init__(obj1, "123", "John", "IFSC001", 1000)
- Inside __init__, you assign:
self.name = "John"  # which means obj1.name = "John"
self.balance = 1000 # which means obj1.balance = 1000
So self is just a name for the current object (obj1), and all attributes like self.name, self.balance are stored inside that object.
Now when you call:
account1.deposit(500)
Python does:
BankAccount.deposit(obj1, 500)
And inside deposit, self again refers to obj1. So self.balance += 500 means:
obj1.balance = obj1.balance + 500 """