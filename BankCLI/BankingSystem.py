from Account import Account
class BankingSystem:
    
    def __init__(self):
        self.accounts = {}
        self.account_Number = 1001
   
    def main_menu(self,account_number):
        while True:    
            print('\n')
            print('Welcome to CLI formatted Banking System !')
            print('Please Choice from the below options :')
            print('\n')
            print('====Main Menu====')
            print('1.Deposit Amount')
            print('2.Withdraw Amount')
            print('3.Check Balance')
            print('4.Show Transactions')
            print('5.Exit')
            print('=================')
                    
            choiceM = int(input('Enter the Choice here ->'))
            if choiceM == 1 :
                print('\nEntering the Depositing System.')
                deposit_amount=int(input('Enter the Deposit Amount :'))
                self.deposit(account_number,deposit_amount)
            elif choiceM ==  2:
                print('\nEntering the Withdrawing System.')
                withdraw_amount = int(input('Enter the withdrawal Amount :'))
                self.withdraw(account_number,withdraw_amount)
            elif choiceM == 3 :
                print('\nGathering the detials to check the current balance.')
                self.check_balance(account_number)
            elif choiceM == 4 :
                print('\nGathering the details of your transactions.')
                self.show_transactions(account_number)
            elif choiceM == 5 :
                print('\nExiting the Banking System. Thank you for using our service.')
                break
            else :
                print('\nInvalid Choice. Please enter a valid option from the menu.')


    def LogInSystem(self,account_number,pin):
        account = self.accounts.get(account_number)
        if not account :
            print('Account not found.')
            return False
        else:
            if account.PIN_NUMBER == pin :
                print('Login Successful.!')
                print('Entering Main Dashboard.')
                self.main_menu(account_number)
            else:
                print('Wrong Credentials.')
                return False

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
    
    def show_transactions(self,account_number):
        account = self.get_account(account_number)
        if not account :
            print('Account not found.')
            return False
        account.show_transactions()