# Solved on 2022. 2. 4.
# 17779 게리맨더링 2

from collections import defaultdict
import sys
input = sys.stdin.readline


def simulation(x, y, d_one, d_two):
    section_five = defaultdict(list)
    section_five[x].append(y)
    for i in range(1, d_one+1):
        section_five[x+i].append(y-i)
        section_five[x+d_two+i].append(y+d_two-i)
    for i in range(1, d_two+1):
        section_five[x+i].append(y+i)
        section_five[x+d_one+i].append(y-d_one+i)
    section_five[x+d_one+d_two].pop()
    for c in section_five.keys():
        section_five[c].sort()
    
    sections = [0] * 6
    for r in range(N):
        for c in range(N):
            if r in section_five:
                if len(section_five[r]) == 1:
                    if section_five[r][0] == c:
                        sections[5] += graph[r][c]
                        continue
                elif section_five[r][0]<=c<=section_five[r][1]:
                    sections[5] += graph[r][c]
                    continue

            if 0<=r<x+d_one and 0<=c<=y:
                sections[1] += graph[r][c]
            elif 0<=r<=x+d_two and y<c<=N-1:
                sections[2] += graph[r][c]
            elif x+d_one<=r<=N-1 and 0<=c<y-d_one+d_two:
                sections[3] += graph[r][c]
            elif x+d_two<r<=N-1 and y-d_one+d_two<=c<=N-1:
                sections[4] += graph[r][c]

    sections.sort()
    
    if sections[1] == 0:
        return 50000
    return sections[-1]-sections[1]


N = int(input())
graph = [[*map(int, input().split())] for _ in range(N)]
MIN = 50000
for x in range(N):
    for y in range(N):
        for d_one in range(1, N+1):
            for d_two in range(1, N+1):
                if x+d_one+d_two > N-1 or y-d_one < 0 or y+d_two > N-1:
                    continue
                MIN = min(MIN, simulation(x, y, d_one, d_two))
print(MIN)
