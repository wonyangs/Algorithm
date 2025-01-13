N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
i = 0
for b in B:
    while b > A[i]: i += 1
    A[i] -= b
print(sum(A))
