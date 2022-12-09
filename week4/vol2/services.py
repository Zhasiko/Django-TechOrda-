from models import BankAccount, Account
from repositories import AccountRepositories


class AccountServices:

    repos: AccountRepositories

    def __init__(self, repos: AccountRepositories):
        self.repos = repos

    def create_account(self, name: str, surname: str, account_type: Account) -> None:
        self.repos.create_account(name=name, surname=surname, account_type=account_type)
        self._send_number_verification(number=name)

    def get_account(self, name: str, surname: str) -> BankAccount | None:
        self.repos.get_account(name=name, surname=surname)

    @staticmethod
    def _send_number_verification(number: str) -> None:
        print(f'verification letter has sended to {number}')