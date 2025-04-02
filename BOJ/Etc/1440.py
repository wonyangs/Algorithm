import sys
import itertools


s = sys.stdin.readline().strip()
a, b, c = s.split(':')


def h(x):
    return 1 <= int(x) <= 12


def m(x):
    return 0 <= int(x) <= 59


r = 0
for p in itertools.permutations([a, b, c]):
    if h(p[0]) and m(p[1]) and m(p[2]):
        r += 1
print(r)
