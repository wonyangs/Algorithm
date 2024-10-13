R, B = map(int, input().split())
for L in range(1, int((R+B)**0.5) + 1):
    if (R+B) % L == 0:
        W = (R+B) // L
        if 2*(L + W) - 4 == R:
            print(max(L, W), min(L, W))
            break
