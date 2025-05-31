while True:
    try:
        a = list(map(float, input().split()))
    except EOFError:
        break
    x1, y1, x2, y2, x3, y3, x4, y4 = a
    if x1 == x3 and y1 == y3:
        sx, sy = x1, y1; px, py = x2, y2; qx, qy = x4, y4
    elif x1 == x4 and y1 == y4:
        sx, sy = x1, y1; px, py = x2, y2; qx, qy = x3, y3
    elif x2 == x3 and y2 == y3:
        sx, sy = x2, y2; px, py = x1, y1; qx, qy = x4, y4
    else:
        sx, sy = x2, y2; px, py = x1, y1; qx, qy = x3, y3
    r1 = px + qx - sx
    r2 = py + qy - sy
    print(f"{r1:.3f} {r2:.3f}")
