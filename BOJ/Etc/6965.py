n = int(input())
for i in range(n):
    s = input().split()
    r = ["****" if len(w) == 4 else w for w in s]
    print(" ".join(r))
    if i < n - 1:
        print()
