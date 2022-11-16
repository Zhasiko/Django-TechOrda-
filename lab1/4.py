n = int(input())
h = 9
m = 0
for i in range(1,n):
    if i % 2 == 1:
        m += 5
    elif i % 2 == 0:
        m += 15
m += 45 * n
res = m // 60
h += res
m -= res * 60

print(h,m)