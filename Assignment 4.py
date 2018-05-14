'''
Kevin Li 1630941
420-LCU Computer Programming, Section 1
Friday, May 15th
S. Hillal, Instructor
Assignment 4
'''
#CLASS
class Account():
    def __init__(self, accountTYPE, bankNAME, balance):
        self.accountTYPE = accountTYPE #The three attributes for each account
        self.bankNAME = bankNAME
        self.balance = balance

#MENU
print("----------------")
print("1- Create an account")
print("2- Delete an account")
print("3- Withdraw from an account")
print("4- Deposit an account")
print("5- Display my account information: Bank Name, Account Type, Balance")
print("6- Log my account information in a file. Include data and time")
print("7- Exit")
print("----------------")
