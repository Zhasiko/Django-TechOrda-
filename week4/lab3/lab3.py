from enum import Enum

accounts = []

class AccountType(Enum):
    EUR = "EUR"
    KZT = "KZT"
    RUB = "RUB"
    USD = "USD"

class BankAccount:
    def __init__(self, name: str, surname: str, account_type: AccountType, cash: int):
        self.name = name
        self.surname = surname
        self.account_type = account_type
        self.cash = cash

    def addToBankAccount(self, summ: int):
        self.cash += summ

    def substractFromBankAccount(self, summ: int):
        if self.cash - summ >= 0:
            self.cash -= summ
        else:
            print("insufficient funds")

    def moneyConversion(self, to: AccountType):
        if self.account_type == AccountType.KZT:
            if to == AccountType.RUB:
                self.cash /= 7.5
                self.account_type = AccountType.RUB
            elif to == AccountType.USD:
                self.cash /= 470
                self.account_type = AccountType.USD
            elif to == AccountType.EUR:
                self.account_type = AccountType.KZT
                self.cash /= 495

        if self.account_type == AccountType.RUB:
            if to == AccountType.KZT:
                self.account_type = AccountType.KZT
                self.cash *= 7.5
            elif to == AccountType.USD:
                self.account_type = AccountType.USD
                self.cash /= 62
            elif to == AccountType.EUR:
                self.account_type = AccountType.EUR
                self.cash /= 66

        if self.account_type == AccountType.USD:
            if to == AccountType.KZT:
                self.account_type = AccountType.KZT
                self.cash *= 470
            elif to == AccountType.RUB:
                self.account_type = AccountType.RUB
                self.cash *= 62
            elif to == AccountType.EUR:
                self.account_type = AccountType.EUR
                self.cash *= 0.95

        if self.account_type == AccountType.EUR:
            if to == AccountType.KZT:
                self.account_type = AccountType.KZT
                self.cash *= 495
            elif to == AccountType.RUB:
                self.account_type = AccountType.RUB
                self.cash *= 66
            elif to == AccountType.USD:
                self.account_type = AccountType.USD
                self.cash *= 1.05



    def __repr__(self):
        return f"{self.name} {self.surname} {self.cash} {self.account_type}"


while True:
    play = input("Please, choose operation\n"
                 "1 - Create Bank Account\n"
                 "2 - Choose Bank Account\n"
                 "3 - Quit\n")

    if play == '3':
        exit(0)

    if play == '1':
        name, surname = input("Please, enter your name and surname\n").split()
        account_type = input("Choose account type:\n"
                             "KZT\n"
                             "USD\n"
                             "RUB\n"
                             "EUR\n")
        if account_type == "KZT":
            account = BankAccount(name=name, surname=surname, account_type=AccountType.KZT, cash=0)
            accounts.append(account)

        elif account_type == "RUB":
            account = BankAccount(name=name, surname=surname, account_type=AccountType.RUB, cash=0)
            accounts.append(account)

        elif account_type == "USD":
            account = BankAccount(name=name, surname=surname, account_type=AccountType.USD, cash=0)
            accounts.append(account)

        elif account_type == "EUR":
            account = BankAccount(name=name, surname=surname, account_type=AccountType.EUR, cash=0)
            accounts.append(account)

        else:
            print('Please, enter again')

    if play == '2':
        if len(accounts) == 0:
            print("Database is empty")
            continue
        for i in range(len(accounts)):
            print(f'{i} - {accounts[i]}')
        account_num = int(input("Chose available account and enter number:\n"))
        account = accounts[account_num]
        print(account)
        while True:
            operation = input(f"Please, choose the operation for {account.name}\n"
                              "1 - add money\n"
                              "2 - substract money\n"
                              "3 - convert money\n"
                              "4 - delete Bank Account\n"
                              "5 - Transaction to other Bank Account\n"
                              "0 - exit to menu\n")

            if operation == '1':
                summ = int(input("Please, enter the sum\n"))
                account.addToBankAccount(summ)
                print(account.name, account.cash, account.account_type)

            if operation == '2':
                summ = int(input("Please, enter the sum\n"))
                account.substractFromBankAccount(summ)
                print(account.name, account.cash, account.account_type)

            if operation == '3':
                typee = input('Please, choose type of Conversion\n'
                             'KZT\n'
                             'EUR\n'
                             'USD\n'
                             'RUB\n')
                account.moneyConversion(typee)
                print(account.name, account.cash, account.account_type)

            if operation == '4':
                print(f'{account.name} is deleted')
                accounts.remove(account)
                del account
                break


            if operation == '0':
                break

            if operation == '5':
                for i in accounts:
                    if i.name == account.name and i.surname == account.surname:
                        continue
                    else:
                        print(i.name, i.surname)
                toAccount = input("Please, enter name and surname of your friend:\n").split()
                for i in accounts:
                    if toAccount[0] == i.name and toAccount[1] == i.surname:
                        summ = float(input("Please, enter the sum:\n"))
                        if summ > account.cash:
                            print("Low money")
                            break
                        else:
                            if account.account_type == i.account_type:
                                i.cash += summ
                                account.cash -= summ
                            else:
                                i_account_type = i.account_type
                                i.moneyConversion(account.account_type)
                                i.cash += summ
                                account.cash -= summ
                                i.moneyConversion(i_account_type)

                            print(f'{account}\n'
                                  f'{i}\n')
                    else:
                        print("User not found")