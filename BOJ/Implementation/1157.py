# Solved on 2021.08.28
# 1157 단어 공부

import sys
input = sys.stdin.readline

isRun = False
maxi = -1
count = [0] * (ord("z")-ord("a")+1)

string = input()
string = string.strip()

for alpha in string:
    if alpha > "Z":
        count[ord(alpha)-ord("a")] += 1
    else:
        count[ord(alpha)-ord("A")] += 1

maxNum = max(count)

for i in range(len(count)):
    if count[i] == maxNum:
        if maxi != -1:
            isRun = True
            break
        else:
            maxi = i

if isRun:
    print("?")
else:
    print(chr(maxi+ord("A")))
