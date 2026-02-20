class BankingServices:

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
        try:
            self.repo.insert_account(new_account_number,name,initial_deposit)
            self.repo.insert_transaction(new_account_number,"INITIAL DEPOSIT",initial_deposit,initial_deposit)
            self.repo.commit()
        except Exception as e:
            self.repo.rollback()
            raise e
        return new_account_number
    
    def deposit(self,account_number,amount):
        account = self.repo.get_account(account_number)
    
        if not account:
            raise ValueError('Account Not Found.')
        if amount <= 0:
            raise ValueError('Amount should be greater than 0.')
        
        balance = account.balance
        new_balance = balance + amount
        
        try:
            self.repo.update_balance(account.account_number,new_balance)
            self.repo.insert_transaction(account_number,"DEPOSIT",amount,new_balance)
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
        if account.balance < amount:
            raise ValueError('Insufficient Balance.')
        
        old_balance = account.balance
        new_balance = old_balance - amount

        try :
            self.repo.update_balance(account.account_number,new_balance)
            self.repo.insert_transaction(account_number,"WITHDRAW",amount,new_balance)
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
