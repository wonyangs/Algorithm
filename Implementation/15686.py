# Solved on 2021. 09. 11.
# 15686 치킨 배달

from itertools import combinations
import sys
input = sys.stdin.readline

# 조건 입력
N, M = map(int, input().split())

array = []

for _ in range(N):
    array.append(list(map(int, input().split())))

# 집, 치킨집 좌표 저장
house = []
store = []

for i in range(N):
    for j in range(N):
        if array[i][j] == 1:
            house.append((i, j))
        if array[i][j] == 2:
            store.append((i, j))


# 선택 가능한 치킨집 조합
comb = list(combinations(store, M))

# 모든 경우의 수 거리 측정
distanceAll = []
for j in range(len(comb)):
    distance = [100] * len(house)
    for i in range(len(house)):
        x = house[i][0]
        y = house[i][1]

        for k in range(M):
            cx = comb[j][k][0]
            cy = comb[j][k][1]

            dis = abs(x-cx) + abs(y-cy)
            distance[i] = min(distance[i], dis)
    distanceAll.append(sum(distance))

# 최단 거리 출력
print(min(distanceAll))

