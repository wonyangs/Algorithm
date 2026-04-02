k = int(input())
p = ["*x*", " xx", "* *"]
for r in p:
    s = "".join(c * k for c in r)
    for _ in range(k):
        print(s)
