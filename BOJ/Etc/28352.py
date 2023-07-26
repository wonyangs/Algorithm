N = int(input())
res = 1
for i in range(1, N+1):
    res *= i
print(res//(7*24*60*60))
