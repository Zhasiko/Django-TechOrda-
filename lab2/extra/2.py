n = int(input())

n1 = 1
n2 = 2
if n == 1:
    print(1)
    exit(0)
if n == 2:
    print(2)
    exit(0)
for i in range(2, n):
    n1, n2 = n2, n1 + n2
print(n2)
