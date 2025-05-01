n = int(input())
s = 2
c = 0
while True:
    l = s - 1
    if c + l >= n:
        idx = n - c - 1
        a = l - idx
        b = idx + 1
        print(a, b)
        break
    c += l
    s += 1
