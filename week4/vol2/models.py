from enum import Enum


class Account(Enum):
    USD = "USD"
    RUB = "RUB"
    KZT = "KZT"
    EUR = "EUR"


class BankAccount:
    cash: float

    def __init__(self, name: str, surname: str, account_type: Account):
        self.name = name
        self.surname = surname
        self.account_type = account_type

    def add_money(self, summa: float):
        self.cash += summa
        return self.cash

    def substract_money(self, summa: float):
        self.cash -= summa
        return self.cash

    def conversion_Money(self, toAccount=Account):
        self.cash


    def __str__(self):
        return f'{self.name} {self.account_type}'

