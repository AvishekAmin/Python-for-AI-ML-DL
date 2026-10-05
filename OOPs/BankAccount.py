# Concept: Classes & Objects

class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            self.balance += amount
            print(f"Amount {amount} deposited successfully!")


    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Amount {amount} withdrawn successfully!")
    
    def check_balance(self):
        return self.balance

b1 = BankAccount(1001, "Avishek Amin", 100_000) 

print(f"{b1.owner_name} has Rs. {b1.balance} in account number: {b1.account_number}")

b1.deposit(2000)
b1.withdraw(1000)
print(f"Current balance: Rs. {b1.check_balance()}")
