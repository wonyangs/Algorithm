import math
n = int(input())
for _ in range(n):
    A1, P1 = map(int, input().split())
    R1, P2 = map(int, input().split())
    if A1/P1 > math.pi*R1*R1/P2:
        print("Slice of pizza")
    else:
        print("Whole pizza")
