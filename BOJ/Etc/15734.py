import sys
L, R, A = map(int, sys.stdin.read().split())
diff = abs(L - R)

if L < R:
    L += min(A, diff)
    A -= min(A, diff)
else:
    R += min(A, diff)
    A -= min(A, diff)

L += A // 2
R += A // 2

print(2 * min(L, R))
