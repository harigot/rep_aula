'''
Make a class that represents a bank account. Create four methods named set_details, display, withdraw and 
deposit.

In the set_details method, create two instance variables : name and balance. The default value for balance 
should be zero. In the display method, display the values of these two instance variables.

Both the methods withdraw and deposit have amount as parameter. Inside withdraw, subtract the amount from 
balance and inside deposit, add the amount to the balance.

Create two instances of this class and call the methods on those instances.
'''



class BankAccount:
    def __init__(self, name = 'default', balance = 0):
        self.name = name
        self.balance = balance

    def set_details(self, name, balance):
        self.name = name
        self.balance = balance
    
    def display(self):
        print(f'Name: {self.name}')
        print(f'Balance: {self.balance}')
    
    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount


user1_account = BankAccount()
user1_account.set_details('John', 100)
user1_account.deposit(50)
user1_account.withdraw(10)
user1_account.display()

user2_account = BankAccount()
user2_account.set_details('clark', 140)
user2_account.deposit(40)
user2_account.withdraw(30)
user2_account.display()
