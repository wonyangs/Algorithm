A, B, C = map(int, input().split())

if B < A:
    B, A = A, B
if C < A:
    C, A = A, C
if C < B:
    B, C = C, B

move = 0
if B < C:
    move += (C - B)
if A < B:
    move += (B - A)

print(move)
