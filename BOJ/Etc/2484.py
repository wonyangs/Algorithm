n = int(input())
res = 0
for _ in range(n):
    a = list(map(int, input().split()))
    cnt = {x: a.count(x) for x in set(a)}
    
    if 4 in cnt.values():
        res = max(res, 50000 + a[0] * 5000)
    elif 3 in cnt.values():
        res = max(res, 10000 + [k for k, v in cnt.items() if v == 3][0] * 1000)
    elif list(cnt.values()).count(2) == 2:
        pair = sorted([k for k, v in cnt.items() if v == 2], reverse=True)
        res = max(res, 2000 + pair[0] * 500 + pair[1] * 500)
    elif 2 in cnt.values():
        res = max(res, 1000 + [k for k, v in cnt.items() if v == 2][0] * 100)
    else:
        res = max(res, max(a) * 100)

print(res)
