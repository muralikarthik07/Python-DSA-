class BankAccount:
    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    #Deposite
    def deposite(self, amount):
        self.balance += amount
        print(f"{amount} is deposited sucessfully, Available balance is {self.balance}")

    #Withdraw method
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficiant balance {self.balance}")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn and available balance is {self.balance}") 

    # check balance
    def check_balance(self):
        print(f"Available balance is {self.balance}")



acct1 = BankAccount(741641, "karthik", 3000)

acct1.check_balance()
acct1.deposite(100000)
acct1.check_balance()