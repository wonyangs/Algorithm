import math

a, b = map(int, input().split())
r, c = map(int, input().split())
a = a / b
r = r * r * math.pi / c

if a < r:
    print("Whole pizza")
else:
    print("Slice of pizza")
