from Transaction import Transaction
class Account:
    def __init__(self,account_number,pin_number,name,amount):
        self.ACCOUNT_NUMBER = account_number
        self.PIN_NUMBER = pin_number
        self.NAME = name
        self.Balance = amount
        self.transactions=[]
    
    def deposit(self,deposit_amount):
        if deposit_amount <= 0:
            print('Amount Number should be A Positive number.')
            return False
        self.Balance += deposit_amount
        transaction = Transaction('Deposit',deposit_amount,self.Balance)
        self.transactions.append(transaction)
        return True
    
    def withdraw(self,withdraw_amount):
        if withdraw_amount <= 0:
            print('Withdrawal amount should be A Positive number.')
            return False
        elif self.Balance < withdraw_amount:
            print('Not enought Balance in your account.')
            return False
        elif self.Balance == 0:
            print('No amount to withdraw from your account.')
            return False
        self.Balance -= withdraw_amount
        transaction = Transaction('Withdraw',withdraw_amount,self.Balance)
        self.transactions.append(transaction)
        return True
    
    def get_balance(self):
        return self.Balance
    
    def get_account_details(self):
        return f"Account Number:{self.ACCOUNT_NUMBER} ,\nName : {self.NAME} ,\nBalance : {self.Balance}\n"
    
    def show_transactions(self):
        if not self.transactions:
            print('No Transaction Found.')
            return False
        for transaction in self.transactions:
            print(transaction)