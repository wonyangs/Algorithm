_, t = map(int, input().split())
print(sum([n <= t for n in [*map(int, input().split())]]))
