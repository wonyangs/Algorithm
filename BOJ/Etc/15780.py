N, K = map(int, input().split())
arr = [*map(int, input().split())]

cnt = 0
for m in arr:
    cnt += (m + 1) // 2
print("YES" if cnt >= N else "NO")
