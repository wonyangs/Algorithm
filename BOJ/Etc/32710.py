s = set()

for i in range(2, 10):
    for j in range(1, 10):
        s.add(i)
        s.add(j)
        s.add(i * j)
N = int(input())
print(1 if N in s else 0)
