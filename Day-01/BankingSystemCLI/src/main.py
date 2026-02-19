from Account import *
from BankingSystem import *
class main(Account,BankingSystem):
    print('Welcome to CLI formatted Banking System !')
    print('Please Choice from the below options :')
    menu ="""====Main Menu===
        1.Login Account
        2.Register Account
        3.Exit"""
    choiceM = int(input(menu))
    if choiceM == 1 :
        print('Entering the Login System.')
        # super.login()
    elif choiceM == 2 :
        print('Entering the Registering System.')
        # super.registerSystem()
    elif choiceM == 3 :
        print('''Exiting the Banking System.
                 Thank You for your time.''')
        