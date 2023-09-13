import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = [input().strip() for _ in range(N)]
s = '0' * K

cnt = 0
for i in range(N):
    for j in range(M - K + 1):
        if arr[i][j:j+K] == s:
            cnt += 1
print(cnt)
