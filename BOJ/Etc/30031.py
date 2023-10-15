res = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == 136:
        res += 1000
    elif a == 142:
        res += 5000
    elif a == 148:
        res += 10000
    else:
        res += 50000
print(res)
