class Account(object):
    'a bank account class'

    def set(self, value):
        'set the balance to value'
        self.balance = value

    def get(self):
        'return the current balance on the account'
        return self.balance

    def deposit(self, value):    
        'updates the bank account by depositing value amount'
        self.balance += value      

    def withdraw(self, value):  
        'updates the bank account by withdrawing value amount'
        self.balance -= value

    def __init__(self, value = 0.0):
        'the constructor'
        self.balance = value

    def __init__(self, value = 0.0):
        'the constructor'
        self.balance = value

    def __repr__(self):
        return f"Account({self.balance})"

    def __str__(self):
        return f"${self.balance:.2f}" 

