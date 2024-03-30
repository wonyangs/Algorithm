def f(N):
    arr = []
    while N:
        arr.append(N % 10)
        N //= 10

    res = 1
    for n in arr:
        res *= n
    return res

N = int(input())
cnt = 0
while N >= 10:
    N = f(N)
    cnt += 1
print(cnt)
