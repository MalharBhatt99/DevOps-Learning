from datetime import datetime
class Transaction:

    def __init__(self,transaction_type,amount,current_balance):
        self.TIMESTAMP = datetime.now()
        self.TRANSACTION_TYPE = transaction_type
        self.AMOUNT= amount
        self.CURRENT_BALANCE = current_balance
    
    def __str__(self):
        return f"{self.TIMESTAMP}|{self.TRANSACTION_TYPE}|{self.AMOUNT}|{self.CURRENT_BALANCE}"

