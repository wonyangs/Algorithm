from math import sqrt,ceil

N = int(input())
arr = []

for i in range(2, ceil(sqrt(N))+ 1):
    while N % i == 0:
        arr.append(i)
        N //= i
if N != 1: arr.append(N)

print(len(arr))
print(*arr)
