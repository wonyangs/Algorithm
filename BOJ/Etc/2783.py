x, y = map(int, input().split())
res = x / y
for _ in range(int(input())):
    x, y = map(int, input().split())
    if res > x / y:
        res = x / y
res *= 1000
print("%.2f"%res)
