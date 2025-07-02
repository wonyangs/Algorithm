n = int(input())
ans = 0

for _ in range(n):
    a = list(map(int, input().split()))
    run = max(a[0], a[1])
    trick = sorted(a[2:], reverse=True)[:2]
    total = run + sum(trick)
    ans = max(ans, total)

print(ans)
