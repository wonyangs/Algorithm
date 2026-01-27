import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

def check(x):
    res = 0
    for n in arr:
        res += n // x
    return res >= K

start, end, answer = 0, 2**31 - 1, -1

while start <= end:
    mid = (start + end) // 2
    
    if check(mid):
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)
