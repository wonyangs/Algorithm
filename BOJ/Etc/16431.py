B, D, J = [*map(int, input().split())], [*map(int, input().split())], [*map(int, input().split())]
b = max(abs(B[0] - J[0]), abs(B[1] - J[1]))
d = abs(D[0] - J[0]) + abs(D[1] - J[1])
print("bessie" if b < d else "daisy" if b > d else "tie")
