def tc():
    N, *arr = map(int, input().split())
    
    line, cnt = [], 0
    for n in arr:
        res = [*filter(lambda x: x >= n, line)]
        cnt += len(res)
        line.append(n)
    print(N, cnt)


N = int(input())

for _ in range(N):
    tc()
