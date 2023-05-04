N, A, B, C, D = map(int, input().split())

set_x = (N + A - 1) // A * B
set_y = (N + C - 1) // C * D

print(min(set_x, set_y))
