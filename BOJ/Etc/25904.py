N, X = map(int, input().split())
arr = [*map(int, input().split())]
i = 0
while True:
    if arr[i] < X:
        break
    i += 1
    if i == N:
        i = 0
print(i + 1)
