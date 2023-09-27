N = int(input())
arr = [*map(int, input().split())]

dp1 = [1] * N
dp2 = [1] * N

before = 0
for i, n in enumerate(arr):
    if i == 0:
        before = n
        continue

    if n < before:
        dp1[i] = 1
    else:
        dp1[i] = dp1[i-1] + 1
    
    if n > before:
        dp2[i] = 1
    else:
        dp2[i] = dp2[i-1] + 1
    before = n

print(max(max(dp1), max(dp2)))
