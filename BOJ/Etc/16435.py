N, s = map(int, input().split())
arr = [*map(int, input().split())]
arr.sort()
for i in arr:
    if i <= s:
        s += 1
print(s)
