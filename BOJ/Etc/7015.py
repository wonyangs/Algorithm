import sys

a = sys.stdin.read().split()
for i in range(1, len(a), 3):
    y, m, d = int(a[i]), int(a[i+1]), int(a[i+2])
    p = (y - 1 - (y - 1) // 3) * 195 + ((y - 1) // 3) * 200
    for j in range(1, m):
        p += 20 if y % 3 == 0 or j % 2 else 19
    print(196470 - p - d + 1)
