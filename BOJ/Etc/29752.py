N = int(input())
arr = [*map(int, input().split())]

MAX = 0
cnt = 0
for n in arr:
    if n != 0:
        cnt += 1
        MAX = max(MAX, cnt)
    else:
        cnt = 0
print(MAX)
