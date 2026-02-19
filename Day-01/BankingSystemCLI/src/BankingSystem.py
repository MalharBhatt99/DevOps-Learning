from Account import *
import random
class BankingSystem(Account) :
    def login(self,account_Number,pin_Number):
        while True:
            print('Welcome to the Login Dashboard :')
            account_Number=input('Enter the Account Number here ->')
            pin_Number = int(input('Enter the Pin Number here ->'))
            
            if(self.ACCOUNT_NUMBER==account_Number) and (self.PIN_NUMBER == pin_Number):
                print('LogIn Successful.')
                print('Operating Main Dashboard :')
            elif self.ACCOUNT_NUMBER != account_Number:
                print('Account doesnot exist.')
                choiceR= input('if You want to register type \'Y\' or else type \'N\':')
                if choiceR == 'Y'or choiceR=='y':
                    print('Entering Registering System.')
                    self.registerSystem()
                elif choiceR == 'N' or choiceR == 'n':
                    print('Existing the Banking System.')
                    exit()
                else :
                    print('Please enter a valid choice.')

    def registerSystem(self,account_Number,pin_Number):
        nextAccountNumber = random.randint(100000,999999)
        print('Welcome to the Registration Dashbaord :')
        print('Your Account Number is :' , nextAccountNumber)
        pin_Number=int(input('Enter the pincode number here ->'))

        