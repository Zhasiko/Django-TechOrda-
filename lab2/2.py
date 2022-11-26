a = int(input())

for i in range(a):
    i += 2
    if a % i == 0:
        print(i)
        break