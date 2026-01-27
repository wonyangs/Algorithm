import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
arr = [*map(int, input().split())]

max_dist = -1
for i in range(M-1):
    max_dist = max(max_dist, arr[i+1] - arr[i])

start_dist, end_dist = arr[0], N - arr[-1]

res = max(start_dist, end_dist, (max_dist + 1) // 2)
print(res)
