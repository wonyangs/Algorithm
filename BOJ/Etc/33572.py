n, m = map(int, input().split())
a = list(map(int, input().split()))
print("DIMI" if sum(x - 1 for x in a) >= m else "OUT")
