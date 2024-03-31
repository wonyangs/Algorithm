T = int(input())
for _ in range(T):
    N = int(input())
    res = 0
    for _ in range(N):
        a, b, c = map(int, input().split())
        res += max(a, b, c, 0)
    print(res)
