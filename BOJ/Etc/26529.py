n = int(input())
f = [1] * 46
for i in range(2, 46):
    f[i] = f[i-1] + f[i-2]
for _ in range(n):
    x = int(input())
    print(f[x])
