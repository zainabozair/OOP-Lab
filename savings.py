from bank import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, account_number, owner, balance=0, interest_rate=0):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest

    def __str__(self):
        return f"{super().__str__()} - Interest rate: {self.interest_rate}%"

 # Create a savings account
savings1 = SavingsAccount(12345, "Alice", 1000, 5)
print("Initial account:", savings1)

# Test inherit deposit method
savings1.deposit(200)
print("After deposit:", savings1)

# Test inherit withdraw method
savings1.withdraw(200)
print("After withdraw:", savings1)

# Apply 5% interest
savings1.apply_interest()
print("After interest:", savings1)
