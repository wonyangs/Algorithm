A = [*map(int, input().split())]
B = [*map(int, input().split())]

while A[1] > 0 and B[1] > 0:
    A[1] -= B[0]
    B[1] -= A[0]

if A[1] <= 0 and B[1] <= 0:
    print("DRAW")
elif A[1] <= 0:
    print("PLAYER B")
else:
    print("PLAYER A")
