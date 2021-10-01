# Solved on 2021. 10. 02.
# 1316 그룹 단어 체커

import sys
input = sys.stdin.readline

n = int(input())
count = 0
for _ in range(n):
    string = list(input().strip())
    check = True
    arr = []
    tmp = string[0]
    arr.append(tmp)

    for c in string:
        if tmp == c:
            check = True
            continue
        else:
            for ch in arr:
                if ch == c:
                    check = False
                    break
                else:
                    tmp = c

        if check is False:
            break
        else:
            arr.append(c)

    if check is True:
        count += 1

print(count)


