n = int(input())
a = list(map(int, input().split()))
p = 1
for x in a:
    if x == p:
        p += 1
print(n - (p - 1))
