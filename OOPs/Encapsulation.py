class BankAccount:
    def __init__(self, name, balance, password):
        self.name = name            # public
        self._balance = balance     # protected
        self.__password = password  # private

    def get_balance(self):      # getter
        return self._balance

    def get_password(self):     # getter
        return self.__password

    def set_balance(self, newBalance):     # setter
        self._balance = newBalance

    def set_password(self, newPassword):    # setter
        self.__password = newPassword

acc1 = BankAccount("Avishek Amin", 100_000, "ABC@123")

print(f"{acc1.name} has Rs. {acc1.get_balance()} and password is: {acc1.get_password()}")
print("After updating values:")
acc1.set_balance(200_000)
acc1.set_password("XYZ@789")
print(f"{acc1.name} has Rs. {acc1.get_balance()} and password is: {acc1.get_password()}")