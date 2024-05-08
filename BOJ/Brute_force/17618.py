N = int(input())
cnt = 0
for i in range(1, N + 1):
    M = i
    res = 0
    while M:
        res += M % 10
        M //= 10
    if i % res == 0:
        cnt += 1
print(cnt)
