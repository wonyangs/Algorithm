N = int(input())
res = 2
for _ in range(N):
    res += res - 1
print(res**2)
