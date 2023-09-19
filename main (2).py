class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        return f"Account Balance for {self.__account_holder_name}: ${self.__account_balance:.2f}"

# Creating an instance of the BankAccount class
account = BankAccount("123456789", "John Doe", 1000.00)

# Testing deposit and withdrawal functionality
print(account.display_balance())  # Display initial balance
account.deposit(500.50)
print(account.display_balance())  # Display updated balance after deposit
account.withdraw(200.75)
print(account.display_balance())  # Display updated balance after withdrawal