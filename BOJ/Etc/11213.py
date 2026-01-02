n = int(input())
a = list(map(int, input().split()))
u = [x for x in a if a.count(x) == 1]
if not u:
    print("none")
else:
    print(a.index(max(u)) + 1)
