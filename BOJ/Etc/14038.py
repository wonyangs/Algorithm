arr = [input() for _ in range(6)]
w = arr.count('W')
if w >= 5:
    print(1)
elif w >= 3:
    print(2)
elif w >= 1:
    print(3)
else:
    print(-1)
