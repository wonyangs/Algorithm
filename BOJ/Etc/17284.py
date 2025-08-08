a = list(map(int, input().split()))
p = {1: 500, 2: 800, 3: 1000}
print(5000 - sum(p[x] for x in a))
