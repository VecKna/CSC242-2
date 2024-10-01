class Account(object):
    'a more complete bank account class'

    # parameter may be non-numeric
    # parameter may be negative
    def __init__(self, val = 0):
        'the constructor'
        assert type(val) == int or type(val) == float, f'{val} not numeric'
        assert val >= 0, 'parameter negative'
        self.balance = val

    # parameter may be non-numeric
    # parameter may be negative
    def set(self, value):
        'set the balance to value'
        assert type(value) == int or type(value) == float, f'{value} not numeric'
        assert value >= 0, 'parameter negative'
        self.balance = value

    def get(self):
        'return the current balance on the account'
        return self.balance

    # parameter may be non-numeric
    # parameter may be negative
    def deposit(self, val):
        'deposit val dollars into the account'
        assert type(val) == int or type(val) == float, f'{val} not numeric'
        assert val > 0, 'parameter not positive'
        self.balance += val

    # parameter may be non-numeric
    # parameter may be negative
    # parameter may be bigger than the balance
    def withdraw(self, value):
        'withdraw value dollars from the account'
        assert type(value) == int or type(value) == float, f'{value} not numeric'
        assert value > 0, 'parameter not positive'
        assert value <= self.balance, 'insufficient funds'
        self.balance -= value

    def __repr__(self):
        'the representation of an Account'
        return f"Account({self.balance})"

    def __str__(self):
        'the string representation of an Account'
        return f"${self.balance:.2f}"

