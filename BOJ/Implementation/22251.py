import sys

input = sys.stdin.readline

arr = [[0, 4, 3, 3, 4, 3, 2, 3, 1, 2], 
[4, 0, 5, 3, 2, 5, 6, 1, 5, 4],
[3, 5, 0, 2, 5, 4, 3, 4, 2, 3], 
[3, 3, 2, 0, 3, 2, 3, 2, 2, 1], 
[4, 2, 5, 3, 0, 3, 4, 3, 3, 2], 
[3, 5, 4, 2, 3, 0, 1, 4, 2, 1], 
[2, 6, 3, 3, 4, 1, 0, 5, 1, 2], 
[3, 1, 4, 2, 3, 4, 5, 0, 4, 3], 
[1, 5, 2, 2, 3, 2, 1, 4, 0, 1], 
[2, 4, 3, 1, 2, 1, 2, 3, 1, 0]]

N, K, P, X = map(int, input().split())

current_floor_str = str(X).zfill(K)
current_digits = [int(d) for d in current_floor_str]

res = 0
for target in range(1, N + 1):
    target_floor_str = str(target).zfill(K)
    target_digits = [int(d) for d in target_floor_str]
    
    cnt = 0
    for i in range(K):
        u = current_digits[i]
        v = target_digits[i]
        cnt += arr[u][v]
    
    if 0 < cnt <= P:
        res += 1

print(res)
