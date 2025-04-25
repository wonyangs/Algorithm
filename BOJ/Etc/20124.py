n = int(input())
a = [input().split() for _ in range(n)]
a.sort(key=lambda x: (-int(x[1]), x[0]))
print(a[0][0])
