while True:
    try:
        d, m, y = map(int, input().split())
    except:
        break
    if d == 0 and m == 0 and y == 0:
        break

    lim = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        lim[2] = 29

    if 1 <= m <= 12 and 1 <= d <= lim[m]:
        print("Valid")
    else:
        print("Invalid")
