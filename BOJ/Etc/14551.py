n, m = map(int, input().split())
r = 1
for _ in range(n):
    a = int(input())
    r = r * (a if a else 1) % m
print(r % m)
