N = int(input())
arr = []
for _ in range(N):
    a, b = map(int, input().split())
    arr.append(a*b)
print(max(arr))
