int(input())
name = list(map(str,input().strip()))

res = 0
for c in name:
    res += ord(c) - ord('A') + 1
print(res)
