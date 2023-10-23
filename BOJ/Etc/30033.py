N = int(input())
A = [*map(int, input().split())]
B = [*map(int, input().split())]
res = 0
for i in range(N):
    if A[i] <= B[i]:
        res += 1
print(res)
