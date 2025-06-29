x, y, p1, p2 = map(int, input().split())
start = max(p1, p2)
end = start + x * y
ans = -1
for i in range(start, end + 1):
    if (i - p1) % x == 0 and (i - p2) % y == 0:
        ans = i
        break
print(ans)
