N = int(input())
arr = [*map(int, input().split())]

cnt = 0
for m in arr:
    if m == cnt % 3:
        cnt += 1
print(cnt)
