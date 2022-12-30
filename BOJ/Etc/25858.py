N, total = map(int, input().split())
arr = [int(input()) for _ in range(N)]
for n in arr:
    print(n * total//sum(arr))
