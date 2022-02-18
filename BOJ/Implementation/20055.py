# Solved on 2022. 2. 18.
# 20055 컨베이어 벨트 위의 로봇

from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
belt = deque([*map(int, input().split())])
robots = []

count = 0
while True:
    count += 1
    
    # 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    belt.rotate(1)
    for i in range(len(robots)):
        robots[i] += 1
    
    for i in range(len(robots)-1, -1, -1):
        if robots[i] == N-1:
            del robots[i]
    
    
    # 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동한다.
    for i in range(len(robots)):
        if robots[i]+1 not in robots and belt[robots[i]+1] > 0:
            robots[i] += 1
            belt[robots[i]] -= 1
            
    for i in range(len(robots)-1, -1, -1):
        if robots[i] == N-1:
            del robots[i]
    
    # 올리는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if belt[0] > 0:
        robots.append(0)
        belt[0] -= 1
    
    for i in range(len(robots)-1, -1, -1):
        if robots[i] == N-1:
            del robots[i]
    
    # 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다.
    if belt.count(0) >= K:
        break
print(count)
