class banking_services:

    #! LOOSE COUPLING CONCEPT APPLIED IN __INIT__()↓
    def __init__(self,repository):
        self.repo=repository


    def create_account(self,name,initial_deposit):
        #name validation
        if not name or not name.strip():
            raise ValueError('Name cannot be empty.')
        #deposit validation
        if initial_deposit<0:
            raise ValueError('Initial Deposit should be greater than 0.')
        #generate account_number    
        last_account_number = self.repo.get_last_account_number()
        if last_account_number is None:
            new_account_number = 1001
        else :
            new_account_number = last_account_number + 1 
        #inserting account
        self.repo.insert_accout(new_account_number,name,initial_deposit)
        return new_account_number
    
    def deposit(self,account_number,amount):
        account = self.repo.get_account(account_number)
        print(type(account))
        
        if not account:
            raise ValueError('Account Not Found.')
        if amount <= 0:
            raise ValueError('Amount should be greater than 0.')
        balance = account[2]
        new_balance = balance + amount
        try:
            self.repo.update_balance(account_number,new_balance)
            self.repo.insert_transaction(account_number,"deposit",amount,new_balance)
            self.repo.commit()
        except Exception as e:
            self.repo.rollback()
            raise e
        return new_balance
    
    def withdraw(self,account_number,amount):
        account = self.repo.get_account(account_number)
        
        if not account:
            raise ValueError('Account not found')
        if amount <= 0:
            raise ValueError('Amount should be greater than 0.')
        if account[2] < amount:
            raise ValueError('Insufficient Balance.')
        
        old_balance = account[2]
        new_balance = old_balance - amount

        try :
            self.repo.update_balance(account_number,new_balance)
            self.repo.insert_transaction(account_number,"withdraw",amount,new_balance)
            self.repo.commit()
        except Exception as e:
            self.repo.rollback()
            raise e
        
        return new_balance
    
    def view_transactions(self,account_number):
        account = self.repo.get_account(account_number)
        if not account:
            raise ValueError('Account not found.')
        transactions_logs =  self.repo.get_transactions(account_number)
        return transactions_logs

