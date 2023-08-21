N = int(input())
arr = []
for _ in range(N):
    name, dd, mm, yy = input().split()
    dd, mm, yy = int(dd), int(mm), int(yy)
    arr.append((yy, mm, dd, name))
arr.sort()
print(arr[-1][3])
print(arr[0][3])
