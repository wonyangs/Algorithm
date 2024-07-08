N, M = map(int, input().split())
arr = [*map(int, input().split())]

res = 0
for i in range(1, N+1):
    flag = False
    for n in arr:
        if i % n == 0:
            flag = True
            break
    if flag:
        res += i
print(res)
