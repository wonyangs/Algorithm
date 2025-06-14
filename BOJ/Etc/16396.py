n = int(input())
s = []

for _ in range(n):
    x, y = map(int, input().split())
    if x > y:
        x, y = y, x
    s.append((x, y))

s.sort()

total = 0
cur_start, cur_end = s[0]

for x, y in s[1:]:
    if x <= cur_end:
        cur_end = max(cur_end, y)
    else:
        total += cur_end - cur_start
        cur_start, cur_end = x, y

total += cur_end - cur_start

print(total)
