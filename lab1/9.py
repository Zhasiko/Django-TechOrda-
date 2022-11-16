a = int(input())
b = int(input())
c = int(input())

if a == b and b == c:
    print(3)
if (a == b and b != c) or (a != b and b == c) or (a == c and a != b):
    print(2)
if a != b and b != c and a != c:
    print(0)