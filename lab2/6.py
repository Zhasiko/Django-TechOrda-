def power(a,b):
    p = 1
    if b == 0:
        print(p)
        return
    for i in range(b):
        p *= a
    print(p)
a,b = input().split()
power(int(a),int(b))