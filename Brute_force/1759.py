# Solved on 2021. 10. 11.
# 1759 암호 만들기

from itertools import combinations
import sys
input = sys.stdin.readline

vowel = set(['a', 'e', 'i', 'o', 'u'])
L, C = map(int, input().split())

charList = list(input().strip().split())
charList.sort()

res = list(combinations(charList, L))

for string in res:
    v = False
    conson = 0
    for i in range(L):
        if string[i] in vowel:
            v = True
        else:
            conson += 1
    if v and conson >= 2:
        print(''.join(string))
