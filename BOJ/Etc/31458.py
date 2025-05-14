t = int(input())
for _ in range(t):
    s = input().strip()
    idx = next(i for i, c in enumerate(s) if c.isdigit())
    n = int(s[idx])
    b = len(s) - idx - 1
    x = 1 if b else n
    if idx % 2:
        x = 1 - x
    print(x)
