P = int(input())
for _ in range(P):
    N, D, A, B, F = map(float, input().split())
    print(f"{int(N)} {F * D / (A + B):.6f}")
