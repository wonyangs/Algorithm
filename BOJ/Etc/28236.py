n, m, k = map(int, input().split())
MIN, CLASS = 1e9, -1
for i in range(1, k+1):
    a, b = map(int, input().split())
    if (dist := a - 1 + n - b) < MIN:
        MIN = dist
        CLASS = i
print(CLASS)
