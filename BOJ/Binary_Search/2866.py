import sys
from collections import defaultdict
input = sys.stdin.readline

R, C = map(int, input().split())
arr = [list(input().strip()) for _ in range(R)]

res = 0
start, end = 0, R - 1
while start <= end:
    mid = (start+end) // 2
    
    check = True
    d = defaultdict(int)
    for j in range(C):
        tmp = ''
        for i in range(mid, R):
            tmp += str(arr[i][j])
        
        if not d[tmp]:
            d[tmp] += 1
        else:
            check = False
            break
    
    if check:
        res = mid
        start = mid + 1
    else:
        end = mid - 1

print(res)
