N = int(input())

a, b = 1, 0
while N:
    a, b = b, a + b
    N -= 1
print(a, b)
