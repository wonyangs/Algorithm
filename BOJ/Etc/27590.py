ds, ys = map(int, input().split())
dm, ym = map(int, input().split())

year = 1
while True:
    if ((year + ds) % ys == 0) and ((year + dm) % ym == 0):
        print(year)
        break
    year += 1
