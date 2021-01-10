# Solved on 2020.12.15
# 1018 체스판 다시 칠하기


import sys
input = sys.stdin.readline


def judge_front(stand, S):
    count = 0
    string = S.copy()
    if stand == 'B':
        if string[0] != 'B':
            count += 1
            string[0] = 'B'
    else:  # stand == 'W'
        if string[0] != 'W':
            count += 1
            string[0] = 'W'

    for i in range(7):
        if string[i] != string[i+1]:
            continue
        else:
            count += 1
            if string[i] == 'B':
                string[i+1] = 'W'
            else:
                string[i+1] = 'B'

    return count


def count_board(L):
    caseB = 0
    caseW = 0
    for i in range(0, 8, 2):
        caseB += judge_front('B', L[i])
        caseB += judge_front('W', L[i+1])
        caseW += judge_front('W', L[i])
        caseW += judge_front('B', L[i+1])
    return min(caseB, caseW)


N, M = map(int, input().split())
a = []
for _ in range(N):
    a.append(list(input().rstrip('\n')))

result = []
for j in range(M-7):
    tmp = []
    for k in range(N):
        tmp.append(a[k][j:j+8])
    for i in range(N-7):
        result.append(count_board(tmp[i:i+8]))

print(min(result))
