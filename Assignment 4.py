'''
Kevin Li 1630941
420-LCU Computer Programming, Section 1
Friday, May 15th
S. Hillal, Instructor
Assignment 4
'''
import datetime

#CLASS
class Account():

    def __init__(self, accountTYPE, bankNAME, balance):
        'Base information for each account'
        self.accountTYPE = accountTYPE #The three attributes for each account
        self.bankNAME = bankNAME
        self.balance = balance

    def __repr__(self):
        'How each account is displayed'
        return ("Account type: {} \nBank name: {} \nBalance: ${}".format(self.accountTYPE,self.bankNAME,self.balance))

    def Withdraw(self):
        'Withdrawing a certain amount from the balance'
        withdraw = input("How much will you be withdrawing?: ")
        if withdraw.isdigit() == False:
            print("Please enter a number")
        else:
            if self.balance >= int(withdraw):
                self.balance -= int(withdraw)
                return "you have ${} left in your bank account".format(self.balance)
            else:
                print("Invalid withdrawal number")

    def Deposit(self):
        'Depositing a certain amount into the balance'
        deposit = input("How much will you be depositing?: ")
        if deposit.isdigit() == False:
            print("Please enter a number")
        else:
            self.balance += int(deposit)
            return "you have ${} left in your bank account".format(self.balance)

AccountList = []
txt = open("MyAccounts.txt","a")

#CREATE AN ACCOUNT
a1 = Account('type','name',90)
a2 = Account('type','name',100)
a3 = Account('type','name',200)
#LIST OF ACCOUNTS
AccountList.append(a1)
AccountList.append(a2)
AccountList.append(a3)
#DELETE AN ACCOUNT
del AccountList[AccountList.index(a3)]
#WITHDRAW FROM AN ACCOUNT
a1.Withdraw()
#DEPOSIT TO AN ACCOUNT
a2.Deposit()
#DISPLAY MY ACCOUNTS INFORMATION: BANK NAME, ACCOUNT TYPE, BALANCE.
print(AccountList)
#LOG MY ACCOUNT INFORMATION IN A FILE. INCLUDE DATE AND TIME
print("{}\n{}\n".format(datetime.datetime.now(),a1), file = txt)
txt.close()
