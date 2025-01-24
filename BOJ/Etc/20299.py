import sys
input = sys.stdin.read
N, K, L, *A = map(int, input().split())
B = [A[i:i+3] for i in range(0, len(A), 3) if min(A[i:i+3]) >= L and sum(A[i:i+3]) >= K]
print(len(B))
print(*sum(B, []))
