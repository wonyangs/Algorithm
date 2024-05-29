import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0] * (N + 1)
for _ in range(M):
    a, b = map(int, input().split())
    arr[a] += 1
    arr[b] += 1
for i in range(1, N+1):
    print(arr[i])
