class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initial_amount, acct_name):
        self.balance = initial_amount
        self.name = acct_name
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def get_balance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print("\nDeposit complete")
        self.get_balance()
     
    def transaction(self,amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}")
        

    def withdraw(self,amount):
        try:
            self.transaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete")
            self.get_balance()
        
        except BalanceException as error:
            print(f"\nWithdraw interrepted: {error}")



    def transfer(self, amount, account):
        try:
            print('\n**********\n\nBeginning Transfer........')
            self.transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)

        except BalanceException as error:
            print(f"\nTransfer interrupted. {error}")