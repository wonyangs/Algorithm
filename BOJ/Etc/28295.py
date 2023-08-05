c = [int(input()) for _ in range(10)]

d = 0
dc = {1: 90, 2: 180, 3: -90}
for i in c:
    d = (d + dc[i]) % 360
dm = {0: 'N', 90: 'E', 180: 'S', 270: 'W'}
print(dm[d])
