n = int(input())
l, r, ans = 1, 10**6, 0
while l <= r:
    m = (l + r) // 2
    if (2 * m**3 + m) // 3 <= n:
        ans = m
        l = m + 1
    else:
        r = m - 1
print(ans)
