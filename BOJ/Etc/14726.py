N = int(input())

for _ in range(N):
    s = [*map(int, input())]
    res = 0
    for i, c in enumerate(s):
        if i % 2 == 0:
            r = int(c) * 2
            if r > 9:
                r = r % 10 + r // 10
        else:
            r = int(c)
        res += r
    print("T" if res % 10 == 0 else "F")
