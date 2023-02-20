MAX = 0
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a == b == c:
        res = 10000 + a * 1000
    elif a == b or b == c:
        res = 1000 + b * 100
    elif a == c:
        res = 1000 + a * 100
    else:
        res = max(a, b, c) * 100
    MAX = max(MAX, res)
print(MAX)
