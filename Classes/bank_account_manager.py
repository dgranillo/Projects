#!/usr/bin/env python2.7
"""Bank Account Manager
Create a class called Account which will be an abstract class for three other
classes called: CheckingAccount, SavingsAccount, and BusinessAccount. Manage
credits and debits from these accounts throough an ATM style program"""

"""TO DO
Clean up the million if statements. Then add functions to different account
types. 

e.g. Interest on savings account's balance determined over time"""

class Account(object):
    num_accounts = 000000000000
    accounts = {}
    def __init__(self, account_balance):
        self.a_bal = account_balance
        self.a_id = Account.num_accounts + 1
        Account.num_accounts += 1
        Account.accounts[self.a_id] = self.a_bal 

    def print_info(self):
        print "Account %012i carries: $%.02f" %(self.a_id, self.a_bal)

    def update_balance(self, amount):
        self.a_bal += amount

class CheckingAccount(Account):
    pass

class SavingsAccount(Account):
    int_rate = 0.90

class BusinessAccount(Account):
    pass

def select_account(accts):
    account_x = int(raw_input("1: Checking, 2: Savings, 3: Business\nSelection: "))
    print Account.accounts[account_x]
    account_func = raw_input("""Would you like to [C]redit/Debit or [T]ransfer
    funds? """)
    amt = int(raw_input("Enter amount: "))
    if account_func.upper() == "C": 
        if account_x == 1:
            my_chk.update_balance(amt)
            my_chk.print_info()
        elif account_x == 2:
            my_sav.update_balance(amt)
            my_sav.print_info()
        elif account_x == 3:
            my_biz.update_balance(amt)
            my_biz.print_info
        else:
            print "Try again!"
            select_account(Account.accounts)
    elif account_func.upper() == "T":
        print "You selected fund Transfer."
        account_y = int(raw_input("Select recipient account: "))
        if account_x == 1:
            my_chk.update_balance(amt*-1)
            my_chk.print_info()
        elif account_x == 2:
            my_sav.update_balance(amt*-1)
            my_sav.print_info()
        elif account_x == 3:
            my_biz.update_balance(amt*-1)
            my_biz.print_info()
        else:
            print "Try again!"
            select_account(Account.accounts)
        if account_y == 1:
            my_chk.update_balance(amt)
            my_chk.print_info()
        elif account_y == 2:
            my_sav.update_balance(amt)
            my_sav.print_info()
        elif account_y == 3:
            my_biz.update_balance(amt)
            my_biz.print_info
        else:
            print "Try again!"
            select_account(Account.accounts)
    else:
        print "You gave the ATM cancer. Try again!"
        select_account(Account.accounts)

        

if __name__ == '__main__':
    my_chk = CheckingAccount(500)
    my_sav = SavingsAccount(453)
    my_biz = BusinessAccount(628.33)

    select_account(Account.accounts)
