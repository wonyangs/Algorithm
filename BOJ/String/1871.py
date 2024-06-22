import sys
input = sys.stdin.readline
from string import ascii_uppercase
alp = list(ascii_uppercase)
for _ in range(int(input())):
    a, b = input().split('-')
    a = alp.index(a[0]) * 26 ** 2 + alp.index(a[1]) * 26 + alp.index(a[2])
    print("nice" if abs(a- int(b)) <= 100 else "not nice")
