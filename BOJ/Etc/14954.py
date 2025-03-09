n = int(input())
v = set()
while n != 1 and n not in v:
    v.add(n)
    n = sum(int(x) ** 2 for x in str(n))
print("HAPPY" if n == 1 else "UNHAPPY")
