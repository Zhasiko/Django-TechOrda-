a = int(input())
b = int(input())
c = int(input())

if b == 0 and c == 0:
    print(0)
    exit(0)
'''
if b == 0:
    if c/a * (-1) > 0:
        print(((c/a) * (-1))**0.5)
        print(((-1) * ((c/a) * (-1)))**0.5)
        exit(0)

if c == 0:
    print(0)
    print(b/a * (-1))
    exit(0)
'''
d = (b**2) - (4*a*c)

if d == 0:
    print((b * (-1)) / (2*a))
    exit(0)

if d > 0:
    print(((b * (-1)) + d**0.5) / (2 * a))
    print(((b * (-1)) - d**0.5) / (2 * a))
    exit(0)