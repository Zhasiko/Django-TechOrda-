s = input()
n = 1
out = 0
for i in s[::-1]:
    if i == '1': out += n
    n <<=1
print(out)