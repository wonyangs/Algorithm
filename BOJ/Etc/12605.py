N = int(input())
for i in range(N):
    arr = list(input().split())[::-1]
    print("Case #%d: "%(i+1), end='')
    print(*arr)
