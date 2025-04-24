n, m = map(int, input().split())
a = [int(input()) for _ in range(n)]
v = [0] * n
for _ in range(m):
    b = int(input())
    for i, x in enumerate(a):
        if x <= b:
            v[i] += 1
            break
print(v.index(max(v)) + 1)
