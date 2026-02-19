from BankingSystem import BankingSystem

bank = BankingSystem()
class main:
    while True:
        print('\n')
        print('Welcome to CLI formatted Banking System !')
        print('Please Choice from the below options :')
        print('\n')
        print('====Main Menu====')
        print('1.Register Account')
        print('2.Deposit Amount')
        print('3.Withdraw Amount')
        print('4.Check Balance')
        print('5.Exit')
        print('=================')
                
        choiceM = int(input('Enter the Choice here ->'))
        if choiceM == 1 :
            print('Entering the Registeration System.')
            name=input('Enter Account Holder Name :')
            pin = int(input('Enter the pin :'))
            deposit_value = int(input('Enter the deposit : '))
            account = bank.registerSystem(name,pin,deposit_value)
            if account :
                print('Account created successfully.!')
                print(account.get_account_details())
        elif choiceM == 2 :
            print('Entering the Depositing System.')
            account_number= int(input('Enter the account number :'))
            deposit_amount=int(input('Enter the Deposit Amount :'))
            bank.deposit(account_number,deposit_amount)
        elif choiceM == 3 :
            print('Entering the Withdrawing System.')
            account_number = int(input('Enter the Account Number :'))
            withdraw_amount = int(input('Enter the withdrawal Amount :'))
            bank.withdraw(account_number,withdraw_amount)
        elif choiceM == 4 :
            print('Gathering the detials to check the current balance.')
            account_number = int(input('Enter the Account Number :'))
            bank.check_balance(account_number)
        elif choiceM == 5 :
            print('Exiting the Banking System. Thank you for using our service.')
            break
        else :
            print('Invalid Choice. Please enter a valid option from the menu.')