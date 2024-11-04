for l in open(0):
    A, B, C = map(int, l.split())
    print(max(C - B, B - A) - 1)
