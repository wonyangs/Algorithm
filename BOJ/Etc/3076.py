R, C = map(int, input().split())
A, B = map(int, input().split())
print('\n'.join([''.join(('X'*B if (i+j)%2==0 else '.'*B) for j in range(C)) for i in range(R) for _ in range(A)]))
