from repository.account_repository import account_repository
from services.banking_services import banking_services

#! DEPENDENCY INJECTION IS ACHIEVED HERE↓
repo = account_repository()
service = banking_services(repo)





# print(service.view_transactions(1016))
