import re
import sys
input = sys.stdin.readline

p = re.compile('(100+1+|01)+')

for _ in range(int(input())):
    print("YES" if p.fullmatch(input().strip()) else "NO")
