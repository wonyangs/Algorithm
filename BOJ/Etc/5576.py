A=[int(input()) for _ in range(10)]
B=[int(input()) for _ in range(10)]
A.sort(reverse=True)
B.sort(reverse=True)
print(sum(A[:3]), sum(B[:3]))
