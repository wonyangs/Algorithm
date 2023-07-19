N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    hap = 0
    for a in range(i-1, x):
        for b in  range(j-1, y):
            hap += arr[a][b]
    print(hap)
