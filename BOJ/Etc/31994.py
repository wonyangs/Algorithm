arr = []

for _ in range(7):
    a, b = input().split()
    b = int(b)
    arr.append((b, a))
arr.sort()
print(arr[-1][1])
