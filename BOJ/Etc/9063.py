A, B = [], []
for _ in range(int(input())):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
print((max(A) - min(A)) * (max(B) - min(B)))
