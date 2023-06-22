t = int(input().strip())
for _ in range(t):
    d = list(map(int, input().split()))
    print("Denominations:", " ".join(map(str, d[1:])))
    if all(d[i] >= 2 * d[i - 1] for i in range(2, len(d))):
        print("Good coin denominations!\n")
    else:
        print("Bad coin denominations!\n")
