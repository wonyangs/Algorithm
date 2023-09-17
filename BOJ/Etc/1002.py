for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = (abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) ** 0.5 
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    else:
        x, y = min(r1, r2), max(r1, r2)
        if dist > y:
            if x + y > dist:
                print(2)
            elif x + y == dist:
                print(1)
            else:
                print(0)
        else:
            if dist + x > y:
                print(2)
            elif dist + x == y:
                print(1)
            else:
                print(0)
