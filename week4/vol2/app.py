from handlers import AccountHandlers
from services import AccountServices
from repositories import AccountRepositories


def init():
    account_repos = AccountRepositories()
    account_services = AccountServices(repos=account_repos)
    account_handlers = AccountHandlers(services=account_services)

    while 1:
        command = input('''
Enter command:
1 - Create Bank Account
2 - Choose Bank Account
0 - Quit
'''
)
        if command == '0':
            exit(0)

        elif command == '1':
            name, surname, account_type = input("Please enter your name, surname and choose account type: ").split()
            account_handlers.sign_up(name=name, surname=surname, account_type=account_type)

        elif command == '2':
            for i in account_repos.accounts:
                print(i)
            name, surname = input("Please choose your account and enter name, surname: ").split()
            account_handlers.sign_in(name=name, surname=surname)

        else:
            print("Invalid command, try again")

if __name__ == '__main__':
    init()
