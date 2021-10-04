# Solved on 2021. 10. 04.
# 16916 부분 문자열

import sys
input = sys.stdin.readline

s = input().strip()
p = input().strip()


def makeTable(string):
    arr = [0] * len(string)
    j = 0
    for i in range(1, len(string)):
        while j > 0 and string[i] != string[j]:
            j = arr[j-1]
        if string[i] == string[j]:
            j += 1
            arr[i] = j
    return arr


def KMP(txt, pat):
    table = makeTable(pat)
    j = 0
    for i in range(len(txt)):
        while j > 0 and txt[i] != pat[j]:
            j = table[j-1]
        if txt[i] == pat[j]:
            if j == len(pat) - 1:
                return True
                j = table[j]
            else:
                j += 1
    return False


if KMP(s, p):
    print(1)
else:
    print(0)
