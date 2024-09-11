N = int(input())
B = list(map(int, input().split()))
A = [B[0]]
for i in range(1, N):
    A.append(B[i] * (i + 1) - sum(A))
print(*A)
