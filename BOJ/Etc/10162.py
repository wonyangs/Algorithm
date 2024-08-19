T = int(input())
A, B, C = 300, 60, 10

if T % C != 0:
    print(-1)
else:
    a = T // A
    b = (T % A) // B
    c = (T % B) // C
    print(a, b, c)
