import sys
input = sys.stdin.readline

N, X, K = map(int, input().split())

arr = [0] * (N + 1)
arr[X] = 1

for _ in range(K):
    a, b = map(int, input().split())
    arr[a], arr[b] = arr[b], arr[a]

print(arr.index(1))
