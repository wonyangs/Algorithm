import sys

input = sys.stdin.readline

arr = [0] * 1000001
N, K = map(int, input().split())
for _ in range(N):
    g, x = map(int, input().split())
    arr[x] = g

hap = 0
prefix = [0]
for n in arr:
    hap += n
    prefix.append(hap)

MAX = 0
for i in range(len(prefix)):
    start, end = max(1, i - K), min(len(prefix) - 1, i + K)
    MAX = max(MAX, prefix[end] - prefix[start-1])

print(MAX)
