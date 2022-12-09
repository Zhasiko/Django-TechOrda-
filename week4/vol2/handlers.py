from models import Account, BankAccount
from services import AccountServices


class AccountHandlers:

    services: AccountServices

    def __init__(self, services: AccountServices):
        self.services = services

    def sign_up(self, name: str, surname: str, account_type: Account) -> None:
        self.services.create_account(name=name, surname=surname, account_type=account_type)

    def sign_in(self, name: str, surname: str) -> BankAccount | None:

        return self.services.get_account(name=name, surname=surname)