from models import BankAccount, Account


class AccountRepositories:
    accounts: list[BankAccount] = []

    def create_account(self, name: str, surname: str, account_type: Account):
        account = BankAccount(name=name, surname=surname, account_type=account_type)

        self.accounts.append(account)

    def get_account(self, name: str, surname: str) -> BankAccount | None:
        account = next(
            (a for a in self.accounts if name == a.name and surname == a.surname),
            None
        )

        if not account:
            print("User not found")

        return account

