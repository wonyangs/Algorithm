N, X = map(int, input().split())
arr = [*map(int, input().split())]
m = 1e9
for i in range(0, N-1):
    if m > arr[i] + arr[i+1]:
        m = arr[i] + arr[i+1]
print(m * X)
