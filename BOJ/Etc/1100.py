# Solved on 2022. 7. 9.
# 1100 하얀 칸

import sys
input = sys.stdin.readline

graph = [[*map(str, input().strip())] for _ in range(8)]
count = 0
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0 and graph[i][j] == 'F':
            count += 1
print(count)
