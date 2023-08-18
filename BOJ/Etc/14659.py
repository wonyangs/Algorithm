import sys
input = sys.stdin.readline

N = int(input())
arr = [*map(int, input().split())]
m = 0
for i in range(N):
    cnt = 0
    for j in range(i+1,N):
        if arr[i] > arr[j]:
            cnt += 1
        else:
            break
    if m < cnt:
        m = cnt
print(m)
        
        
