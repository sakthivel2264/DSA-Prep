
# ABstraction

# Data abstraction is one of the most essential concepts of Python OOPs which is used to hide irrelevant details from the user and show the details that are relevant to the users.

from abc import ABC, abstractmethod

# Abstract base class
class BankAccount(ABC):
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self._balance = 0 # Protected attribute
        
        
    @abstractmethod
    def deposit(self, amount):
        pass
    
    @abstractmethod
    def withdraw(self, amount):
        pass
    
    def get_balance(self):
        return self._balance
    
    
# Concrete class
class SavingsAccount(BankAccount):
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self._balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ₹{amount}. Remaining balance: ₹{self._balance}")
        else:
            print("Invalid or insufficient funds.")
            
        
# Usage
account = SavingsAccount("Alice")
account.deposit(1000)
account.withdraw(300)
print("Final Balance:", account.get_balance())