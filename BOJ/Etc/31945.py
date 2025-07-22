t = int(input())
for _ in range(t):
    a, b, c, d = map(int, input().split())
    s = [a, b, c, d]
    ax = {i // 4 for i in s}
    ay = {(i // 2) % 2 for i in s}
    az = {i % 2 for i in s}
    print('YES' if len(ax) == 1 or len(ay) == 1 or len(az) == 1 else 'NO')
