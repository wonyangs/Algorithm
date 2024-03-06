import sys
input = sys.stdin.readline

N, M = map(int, input().split())

for _ in range(N):
    S = input().strip()
    
    arr = [-1] * M
    cnt = -1
    for i, c in enumerate(S):
        if c == 'c':
            cnt = 0
            arr[i] = cnt
        elif cnt != -1:
            cnt += 1
            arr[i] = cnt
    print(*arr)
