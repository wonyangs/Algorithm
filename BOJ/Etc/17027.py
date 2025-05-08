n = int(input())
ops = [tuple(map(int, input().split())) for _ in range(n)]

res = 0

for start in range(1, 4):
    pos = start
    score = 0
    for a, b, g in ops:
        if pos == a:
            pos = b
        elif pos == b:
            pos = a
        if pos == g:
            score += 1
    res = max(res, score)

print(res)
