L, N = int(input()), int(input())
R = [tuple(map(int, input().split())) for _ in range(N)]
E = [K-P+1 for P, K in R]
C = [0] * (L+1)
A = [0] * N
for i, (P, K) in enumerate(R):
    for j in range(P, K+1):
        if not C[j]:
            C[j] = i+1
            A[i] += 1
print(E.index(max(E)) + 1, A.index(max(A)) + 1, sep='\n')
