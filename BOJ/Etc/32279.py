n = int(input())
p, q, r, s = map(int, input().split())
a = [0] * (n + 1)
a[1] = int(input())

for i in range(2, n + 1):
    if i % 2 == 0:
        a[i] = p * a[i // 2] + q
    else:
        a[i] = r * a[i // 2] + s

print(sum(a[1:n + 1]))
