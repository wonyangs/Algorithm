N = int(input())
res = 0
for i in range(1, N+1):
    if N % i == 0:
        res += i
print(res)
