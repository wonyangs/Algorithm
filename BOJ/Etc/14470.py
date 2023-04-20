A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

time = 0

if A < 0:
    time += -A * C
    time += D

time += (B - max(0, A)) * E

print(time)
