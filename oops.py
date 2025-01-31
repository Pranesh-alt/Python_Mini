from bank_accounts import *
  
Pranesh = BankAccount(1000,"Pranesh")
Ragu = BankAccount(2000,"Ragu")


Pranesh.get_balance()
Ragu.get_balance()

Pranesh.deposit(500)
Ragu.deposit(2)

Pranesh.withdraw(100)
Pranesh.transfer(200,Ragu)