ax, ay, r1 = map(int, input().split())
bx, by, r2 = map(int, input().split())
if (abs(ax - bx) ** 2 + abs(ay - by) ** 2) ** 0.5 < r1 + r2:
    print("YES")
else:
    print("NO")
