A, B = list(map(int, input().split())), list(map(int, input().split()))
a, b, last = 0, 0, 'D'
for i in range(10):
    if A[i] > B[i]: a, last = a+3, 'A'
    elif A[i] < B[i]: b, last = b+3, 'B'
    else: a, b = a+1, b+1
print(a, b)
print(last if a == b else 'A' if a > b else 'B')
