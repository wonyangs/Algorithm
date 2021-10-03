# Solved on 2021. 10. 03.
# 1541 잃어버린 괄호

import sys
input = sys.stdin.readline

string = input().strip()
num = []
label = []

start = 0
for i in range(len(string)):
    if string[i] == '+':
        num.append(int(string[start:i]))
        label.append('+')
        start = i+1
    if string[i] == '-':
        num.append(int(string[start:i]))
        label.append('-')
        start = i+1

num.append(int(string[start:len(string)]))

a = b = 0
a += num[0]
minus = False

for i in range(len(label)):
    if minus is True:
        b += num[i+1]
    else:
        if label[i] == '-':
            minus = True
            b += num[i+1]
        else:
            a += num[i+1]

print(a-b)
