
#h This is a simple and random project idea to see myself on how far i have come to my programming journey.

#&Create a simple banking system that allows users to create accounts, deposit and withdraw money, and check their balance.
#& The system should have the following features:
#& 1. Create an account: The user should be able to create a new account by providing their name and an initial deposit amount.
#& 2. Deposit money: The user should be able to deposit money into their account by providing the account number and the amount to deposit.
#& 3. Withdraw money: The user should be able to withdraw money from their account by providing the account number and the amount to withdraw. The system should check if the account has sufficient funds before allowing the withdrawal.
#& 4. Check balance: The user should be able to check their account balance by providing the account number.
#& 5. Exit: The user should be able to exit the system.

class LogIn(RegisterAccount):
    def login(self,account_number,pin):
        account_number=input('Enter the account number :')
        pin = input('Enter the Pin:')
        if (self.ACCOUNT_NUMBER == account_number) and (self.PIN == pin) :
            print('You have successfully Logged In.')
            super().bankingSystem(account_number,pin)
        elif self.ACCOUNT_NUMBER != account_number:
            print('Account is invalid.Please Register the Account.')
            choiceR = input('Press \'Y\' to Register for a new account or Press \'N\' to retry and \'E\' to Exit :')
            if choiceR == 'Y' or 'y':
                super().registerSystem()
            elif choiceR == 'N' or 'n':
                self.login()
            elif choiceR == 'E' or 'e':
                print('Terminating the process.')
                return 0
        elif self.PIN != pin :
            print('Invalid Credentials.Please Try again.')
            self.login()
        else :
            print('Invalid Input. Please Try again.')
            self.login()


        
class RegisterAccount :
    def registerSystem():
        print('Welcome to Registration :')
        

