m, n = map(int, input().split())
if m == 0:
    print("0")
else:
    s = ""
    while m:
        r = m % n
        s = (chr(r + 55) if r > 9 else str(r)) + s
        m //= n
    print(s)
