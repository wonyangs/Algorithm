a, b = map(int, input().split())
k, x = map(int, input().split())

cnt = 0
for i in range(a, b + 1):
    if abs(k - i) <= x:
        cnt += 1
if cnt != 0:
    print(cnt)
else:
    print("IMPOSSIBLE")
