# Solved on 2020.12.13
# 1181 단어 정렬

from queue import PriorityQueue

que = PriorityQueue()

L = []

N = int(input())  # 단어의 개수

for i in range(N):  # 단어 입력
    a = input()
    L.append(a)

sL = list(set(L))  # 중복 제거

for i in range(len(sL)):
    que.put((len(sL[i]), sL[i]))

for i in range(len(sL)):
    print(que.get()[1])
