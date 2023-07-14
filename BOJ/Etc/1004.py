import math

def is_inner(x, y, cx, cy, r):
    dist = math.sqrt((x - cx) ** 2 + (y - cy) ** 2)
    return dist < r

T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    count = 0
    N = int(input())
    for _ in range(N):
        cx, cy, r = map(int, input().split())
        if is_inner(x1, y1, cx, cy, r) and is_inner(x2, y2, cx, cy, r):
            continue
        elif is_inner(x1, y1, cx, cy, r) or is_inner(x2, y2, cx, cy, r):
            count += 1
        else:
            continue
    print(count)
