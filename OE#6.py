class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance
   
    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")
   
    def withdraw(self, amount: float):
        if 0 < amount <= self.__balance:  
            self.__balance -= amount
        else:
            print("Withdrawal amount must be positive and not exceed the current balance.")
   
    def display_account_info(self):
        print(f"Account Number: {self.__account_number}")
        self.__display_balance()
   
    def __display_balance(self):
        print(f"Current Balance: {self.__balance}")  
   
    def get_account_number(self):
        return self.__account_number
   
    def get_balance(self):
        return self.__balance  
   
    def set_balance(self, balance: float):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Balance cannot be negative.")


account = BankAccount("101", 1000.0)
account.deposit(500.0)        
account.withdraw(200.0)      
account.set_balance(300.0)    
account.display_account_info()  
print(f"Check Balance: {account.get_balance()}")  
