import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
  r, c = map(int, input().split())
  grid = [list(map(int, input().split())) for _ in range(r)]

  rotated = list(zip(*grid))
  res = 0
  for col in range(c):
    floor = r - 1
    for row in range(r - 1, -1, -1):
      if rotated[col][row]:
        res += floor - row
        floor -= 1
  print(res)
