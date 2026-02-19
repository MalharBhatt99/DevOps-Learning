from Account import Account
class BankingSystem:
    def __init__(self):
        self.accounts = {}
        self.account_Number = 1001

    def registerSystem(self,name,pin,initial_deposit_value):
        if not name.strip():
            print('Name cannot be Empty.')
            return False
        if initial_deposit_value < 2000 :
            print('Deposit Value should be minimum ₹2000.')
            return False
        if not isinstance(pin, int) or pin <= 0:
            print('Pin must be a positive integer.')
            return False
        account = Account(self.account_Number,pin,name,initial_deposit_value)
        self.accounts[self.account_Number] = account
        self.account_Number += 1
        return account
    
    def get_account(self,account_number):
        return self.accounts.get(account_number)
    
    def deposit(self,account_number,deposit_value):
        account = self.get_account(account_number)
        if not account:
            print('Account not Found.')
            return False
        account.deposit(deposit_value)
    
    def withdraw(self,account_number,withdraw_value):
        account = self.get_account(account_number)
        if not account:
            print('Account not found.')
            return False
        account.withdraw(withdraw_value)
    
    def check_balance(self,account_number):
        account = self.get_account(account_number)
        if not account:
            print('Account not Found.')
            return False
        print('Balance is :',account.get_balance())
