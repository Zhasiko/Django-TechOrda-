money = 500
f = "KZT"

def addToBankAccount(n):
    global money
    money += n
    print(money)
    
def substractFromBankAccount(n):
    global money
    money -= n
    print(money)
    
def moneyConversion(money, to , f):
    if to == 'USD' and f == 'KZT':
        print(money / 470)
        f = "USD"
    if to == "KZT" and f == "USD":
        print(money*470)
        f = "KZT"



a = input("Please choose bank operation: 1 - Add, 2 - Substract, 3 - Conversion: ")

if a == '1':
    n = int(input("sum: "))
    addToBankAccount(n)
if a == '2':
    n = int(input("sum: "))
    substractFromBankAccount(n)
if a == '3':
    to = input("choose: USD, KZT: ")
    f = input("choose KZT, USD: ")
    moneyConversion(money, to,f)