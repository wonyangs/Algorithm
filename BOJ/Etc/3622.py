A, a, B, b, P = map(int, input().split())
if (A <= b and B <= P) or (B <= a and A <= P) or (A + B <= P):
    print("Yes")
else:
    print("No")
