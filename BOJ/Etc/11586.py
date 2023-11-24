N = int(input())
arr = [input() for _ in range(N)]
t = int(input())
if t == 1:
    for t in arr:
        print(t)
elif t == 2:
    for t in arr:
        print(t[::-1])
else:
    for t in arr[::-1]:
        print(t)
