# This is an example of encapsulation

# In this first example, we are using poor encapsulation
class Account:
    
    def __init__(self):
        self.balance = 0
    
    def deposit(self, amount):
        self.balance = self.balance + amount

account = Account() # Here we call the Account() class to use the code there
account.balance = 50 # Here we define an amount for the 'account.balance' variable which is the 'account' variable and the 'self.balance' variable from the 'Account()' class.
account.deposit(100) # This calls the 'deposit' function and sends it the 'amount' of '100' which it then adds to 'self.balance' which is now 'account.balance'.

print(f"This is the account.balance - {account.balance}")

# The problem in the above code is if we change the balance attribute in the Account() class to keep a list instead of 0
# the entire following code will break. That means it was not well encapsulated.
# It's cool how it works, but it's not following Object Oriented programming.

# Now we will better encapsulate our code. We can use 'Access Modifiers' to specify which attributes and methods are public or private.
# Public class members are accessible from anywhere in the program.
# Private class members are only accessible by methods in teh class that contains them.
# Here we will use the '_' underscore prefix to treat a class member as private.

class Account:

    def __init__(self): # That's a double underscore '_' before and after 'init'
        self._transactions = [] # The '_' prefix means treat this as private.

    def deposit(self, amount):
        self._transactions.append(amount)

# I don't know how to use the above class, but it is better encapsulated. -Matt




