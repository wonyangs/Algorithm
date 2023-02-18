while True:
    a, b, c = input().split()
    b, c = int(b), int(c)
    if a == '#' and b == 0 and c == 0:
        break
    if b > 17 or c >= 80:
        print(a + ' Senior')
    else:
        print(a + ' Junior')
