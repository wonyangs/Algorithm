import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

def check(K):
    count, left = 0, 0
    for n in arr:
        if left < n:
            count += 1
            left = K
        left -= n
    return count <= M

start, end = max(arr), int(1e10)
answer = -1
while start <= end:
    mid = (start + end) // 2
    if check(mid):
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)
