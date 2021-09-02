# Solved on 2021. 09. 02.
# 1343 폴리오미노

import sys
input = sys.stdin.readline

board = list(input())
count = 0
start = 0
end = 0
error = False

for i in range(len(board)):
    if board[i] == 'X':
        if count == 0:
            start = i

        count += 1
    else:
        if count != 0:
            end = i-1
            length = end - start + 1
            if length % 2 == 0:
                for j in range(length // 4):
                    for k in range(4):
                        board[start + k + 4*j] = 'A'
                for j in range(length % 4):
                    for k in range(2):
                        board[end - k] = 'B'
            else:
                error = True
            count = 0

if error:
    print(-1)
else:
    for i in board:
        print(i, end="")
