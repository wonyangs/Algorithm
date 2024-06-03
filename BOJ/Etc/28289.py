N = int(input())
arr = [0] * 4
for _ in range(N):
    g, c, n = map(int, input().split())
    if g == 1:
        arr[-1] += 1
        continue
    
    if c == 1 or c == 2:
        arr[0] += 1
    elif c == 3:
        arr[1] += 1
    else:
        arr[2] += 1

for i in range(4):
    print(arr[i])
