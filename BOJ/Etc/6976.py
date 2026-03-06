import sys

d = sys.stdin.read().split()
if d:
    n = int(d[0])
    for i in range(1, n + 1):
        if i > 1:
            print()
        s = d[i]
        x = int(s)
        while x > 99:
            print(x)
            x = (x // 10) - (x % 10)
        print(x)
        if x % 11 == 0:
            print(f"The number {s} is divisible by 11.")
        else:
            print(f"The number {s} is not divisible by 11.")
