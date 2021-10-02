# Solved on 2021. 10. 02.
# 1316 그룹 단어 체커

import sys
input = sys.stdin.readline

n = int(input())
count = n

for _ in range(n):
    string = list(input().strip())

    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            pass
        elif string[i] in string[i+1:]:
            count -= 1
            break

print(count)
