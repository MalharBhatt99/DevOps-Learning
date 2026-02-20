from repository.account_repository import AccountRepository
from services.banking_services import BankingServices

#! DEPENDENCY INJECTION IS ACHIEVED HERE↓
repo = AccountRepository()
service = BankingServices(repo)




transactions = service.view_transactions(1003)
for t in transactions:
    print(t.transaction_type,t.amount,t.balance_after)

