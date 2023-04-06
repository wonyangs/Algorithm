N = int(input())
arr = [*map(int, input().split())]
arr.sort()
a = arr[:N]
b = arr[N:]
b.reverse()
arr = []
for i in range(N):
    arr.append(a[i] + b[i])
arr.sort()
print(arr[0])
