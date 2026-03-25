import sys

v = sys.stdin.read().split()
for x in v[1:]:
    n = int(x)
    while 1:
        n += 1
        if '0' not in str(n):
            print(n)
            break
