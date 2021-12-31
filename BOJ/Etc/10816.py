# Solved on 2020.12.14
# 10816 숫자 카드 2

import sys
from collections import Counter
input = sys.stdin.readline


_ = input()
a = input().split()
_ = input()
b = input().split()


c = Counter(a)
print(' '.join(f'{c[m]}' if m in c else '0' for m in b))
