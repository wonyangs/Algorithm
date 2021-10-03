# Solved on 2021. 10. 03.
# 2941 크로아티아 알파벳

import sys
input = sys.stdin.readline

cAlpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

string = input().strip()

for c in cAlpha:
    string = string.replace(c, '0')

print(len(string))
