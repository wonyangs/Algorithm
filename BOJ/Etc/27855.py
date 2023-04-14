a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
res = a1 * 3 + b1 - (a2 * 3 + b2)
if res > 0:
    print(1, res)
elif res < 0:
    print(2, -res)
else:
    print("NO SCORE")
