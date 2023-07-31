arr = [[*map(int, input().split())] for _ in range(9)]

m = 0
x, y = 0, 0
for i in range(9):
    for j in range(9):
        if m < arr[i][j]:
            m = arr[i][j]
            x, y = i, j
print(m)
print(x+1, y+1)
