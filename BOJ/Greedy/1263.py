import sys
input = sys.stdin.readline

N = int(input())
works = [tuple([*map(int, input().split())]) for _ in range(N)]
works.sort(key=lambda x: (-x[1], -x[0]))

left_time = works[0][1]

fail = False
for t, end_time in works:
    left_time = min(end_time, left_time)
    left_time -= t
    if left_time < 0:
        fail = True
        break

print(-1 if fail else left_time)
