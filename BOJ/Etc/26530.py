for _ in range(int(input())):
    res = 0
    for __ in range(int(input())):
        a, b, c = input().split()
        b, c = int(b), float(c)
        res += b * c
    print("$%.2f"%res)
