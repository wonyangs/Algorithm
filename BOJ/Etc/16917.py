A, B, C, X, Y = map(int, input().split())
print(min(A*X + B*Y, C*2*max(X, Y), C*2*min(X, Y) + A*(X-min(X, Y)) + B*(Y-min(X, Y))))
