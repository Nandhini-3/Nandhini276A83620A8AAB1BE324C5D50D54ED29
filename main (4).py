class BankAccount:


  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
    self.__account_number = account_number 
    self.__account_holder_name = account_holder_name 
    self.__account_Balance = initial_balance 

  def deposit(self, amount):
    if amount > 0:
      self.__account_Balance += amount 
      print("Deposit ₹{}. New Balance: ₹{}".format(amount, self.__account_Balance))
    else:
     print("Invalid deposit amount . please deposit a positive account.")

  
  def withdraw(self, amount):
    if amount > 0 and amount <= self.__account_Balance:
      self.__account_Balance -= amount       
      print("withdrew ₹{}. New balance: ₹{}".format(amount, self.__account_Balance))
      
    else:
      print("Invalid withdraw amount or insufficient balance.")

  
  def display_balance(self):
    print("Account balance for {}(Account #{}): ₹{}".format(
       self.__account_holder_name, self.__account_number,
      self.__account_Balance))


account = BankAccount(account_number="123456789",account_holder_name="Hari Prabu",  initial_balance=5000.0)

account.display_balance()
account.deposit(5000.0)
account.withdraw(200.0)