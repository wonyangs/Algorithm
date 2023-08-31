import sys
input = sys.stdin.readline

for _ in range(int(input())):
    arr = sorted([tuple(map(int, input().split())) for __ in range(int(input()))])
    MIN, cnt = 1e9, 0
    for a, b in arr:
        if MIN > b:
            MIN = b
            cnt += 1
    print(cnt)
