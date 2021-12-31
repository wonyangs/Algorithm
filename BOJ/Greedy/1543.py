# Solved on 2021. 09. 06.
# 1543 문서 검색

import sys
input = sys.stdin.readline

note = list(input().strip())
key = list(input().strip())

count = 0
i = 0

while(i < len(note)):
    match = True
    if note[i] == key[0]:
        for j in range(len(key)):
            if i+j >= len(note):
                match = False
                break
            if note[i+j] != key[j]:
                match = False
                break
    else:
        match = False

    if match:
        count += 1
        i += len(key)
    else:
        i += 1

print(count)
