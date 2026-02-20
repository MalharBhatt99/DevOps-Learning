import sqlite3
import os
from datetime import datetime

class account_repository:
    
    def __init__(self):

        #!PATH HANDLING↓
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        DB_PATH = os.path.join(BASE_DIR,"..","database","accounts.db")

        self.conn = sqlite3.connect(DB_PATH)
        self.c = self.conn.cursor()

    def get_account(self,account_number):
        self.c.execute("""select account_number,account_holder_name,balance
                    from accounts 
                    where account_number = ?""",(account_number,))
        record = self.c.fetchone()
        return record
    
    def insert_accout(self,account_number,name,balance):
        created_at = datetime.now().isoformat()
        self.c.execute("""insert into accounts (account_number, account_holder_name, balance,created_at) values(? , ? , ? , ?)""",(account_number , name , balance , created_at))
        self.insert_transaction(account_number,"Initial Deposit",balance,balance)
        self.conn.commit()

    def update_balance(self,account_number,new_balance):
        self.c.execute("""update accounts 
                       set balance = ? 
                       where account_number = ?"""
                       ,(new_balance,account_number))
        
#!After insert_transaction(), → Proper separation
#!     we achieve.            → Audit trail capability
#!                            → Foundation for atomic transactions ↓
    def insert_transaction(self,account_number,type,amount,balance_after):
        timestamp = datetime.now().isoformat()
        self.c.execute("""insert into transactions (account_number,type,amount,balance_after,timestamp) values (?,?,?,?,?)""",(account_number,type,amount,balance_after,timestamp))
    
    def get_last_account_number(self):
        self.c.execute("select max(account_number) from accounts")
        last_acc_no= self.c.fetchone()
        if last_acc_no is None or last_acc_no[0] is None:
            return None
        return last_acc_no[0]
    
    def get_transactions(self,account_number):
        self.c.execute("""select * from transactions where account_number = ? order by timestamp DESC""",(account_number,))
        return self.c.fetchall()
    
    def commit(self):
        self.conn.commit()
    
    def rollback(self):
        self.conn.rollback()
    
    def close(self):
        self.conn.close()

#NOTE :
#?What is Repository Responsible For?
#? Repository only:→Talks to database,→Executes SQL,→Returns raw data.

#?Where should the database path logic go? Inside constructor or outside?
#?→ constructor — because connection belongs to repository instance.

#?Should repository check if account already exists?
#?→ No. That’s service layer responsibility.

#?Should repository generate account number?
#?→ No. Service layer responsibility.

#?Should repository commit automatically?
#?→ Yes for account creation (since it's a single operation).
