class InsufficientFundsError(Exception):
    pass

class BankAccount:

    def __init__(self, account_number, owner, balance=0):
        self.account_number=account_number
        self.owner=owner
        self.balance = balance

    def deposit(self, amount):
        if amount <=0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds.")

        self.balance -= amount
        return self.balance    

    def __str__(self):
        return f"Account: {self.account_number} - Owner: {self.owner}, Balance: ${self.balance}"

# Create an account with an initial balance of $500
if __name__ == "__main__":

    account1 = BankAccount(12345, "Alice", 500)
    print(account1)

    # Test deposit
    account1.deposit(200)
    print("After deposit:", account1)

    #Test withdrawal
    account1.withdraw(100)
    print("After withdraw:", account1)

    try:
        account1.withdraw(1000)

    except InsufficientFundsError as e:
        print("Error:", e)
    except ValueError as e:
        print("Error:", e)

    try:
        account1.withdraw(-50)
    except ValueError as e:
        print("Error:", e)


