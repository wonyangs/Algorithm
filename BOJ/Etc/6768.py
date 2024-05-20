import math

J = int(input())
print(0 if J <= 3 else math.comb(J-1, 3))
