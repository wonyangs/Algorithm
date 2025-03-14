while True:
    s = input().strip()
    if not s: continue
    b, op, a = s.split()
    b = int(b)
    a = int(a)
    if b == 0 and op == 'W' and a == 0:
        break
    if op == 'W':
        if b - a < -200:
            print("Not allowed")
        else:
            print(b - a)
    else:
        print(b + a)
