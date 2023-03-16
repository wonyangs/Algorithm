N = int(input())
res = 1
for i in range(1, N+1):
    res *= i
    res %= 10
print(res)
