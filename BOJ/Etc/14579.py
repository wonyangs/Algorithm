a, b = map(int, input().split())
start = 0
for i in range(1, a+1):
    start += i
    
res = 1
for i in range(a, b+1):
    res *= start
    res %= 14579
    start += i + 1

print(res)
