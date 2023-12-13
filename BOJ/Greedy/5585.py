N = 1000 - int(input())
arr = [500, 100, 50, 10, 5, 1]
res = 0

for n in arr:
    div = N // n
    res += div
    N -= div * n

print(res)
