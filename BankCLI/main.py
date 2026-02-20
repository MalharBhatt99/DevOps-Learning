from BankingSystem import BankingSystem

bank = BankingSystem()
class main:
    while True:
        print('\n')
        print('Welcome to CLI formatted Banking System !')
        print('Please Choice from the below options :')
        print('\n')
        print('====Main Menu====')
        print('1.LogIn Account')
        print('2.Register Account')
        print('3.Exit')
        print('=================')
        
        choice = int(input('Enter the Choice here ->'))
        if choice == 1 :
            print('\nEntering the Log-IN System.')
            account_number=int(input('Enter Account Number :'))
            pin = int(input('Enter the pin :'))
            account = bank.accounts.get(account_number)
            if account:
                print('Entering LogIn System.')
                bank.LogInSystem(account_number,pin)
            else :
                print('Account not found.')
        elif choice == 2 :
            print('\nEntering the Registeration System.')
            name=input('Enter Account Holder Name :')
            pin = int(input('Enter the pin :'))
            deposit_value = int(input('Enter the deposit : '))
            account = bank.registerSystem(name,pin,deposit_value)
            if account :
                print('Account created successfully.!')
                print(account.get_account_details())
        elif choice == 3:
            print('Exiting the Banking System. Thank you for using our service.')
            break
        else :
                print('Invalid Choice. Please enter a valid option from the menu.')
