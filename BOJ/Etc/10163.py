n = int(input().strip())
papers = []
max_x = 0
max_y = 0

for _ in range(n):
    x, y, w, h = map(int, input().split())
    papers.append((x, y, w, h))
    max_x = max(max_x, x + w)
    max_y = max(max_y, y + h)

rows = [[(0, max_x, 0)] for _ in range(max_y)]

for i, (x, y, w, h) in enumerate(papers, start=1):
    l = x
    r = x + w
    for row in range(y, y + h):
        new_ints = []
        for a, b, idx in rows[row]:
            if b <= l or a >= r:
                new_ints.append((a, b, idx))
            else:
                if a < l:
                    new_ints.append((a, l, idx))
                new_ints.append((max(a, l), min(b, r), i))
                if b > r:
                    new_ints.append((r, b, idx))
        merged = []
        for seg in new_ints:
            if merged and merged[-1][2] == seg[2] and merged[-1][1] == seg[0]:
                merged[-1] = (merged[-1][0], seg[1], seg[2])
            else:
                merged.append(seg)
        rows[row] = merged

areas = [0] * (n + 1)
for row in rows:
    for a, b, idx in row:
        if idx:
            areas[idx] += b - a

for i in range(1, n + 1):
    print(areas[i])
