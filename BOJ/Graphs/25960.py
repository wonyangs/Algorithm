# Solved on 2022. 11. 20.
# 25960 폰의 각성

from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def parse_graph_info(info_table):
	graph_info = {}
	count = 0
	for i in range(N):
		for j in range(N):
			if table[i][j] != '0':
				graph_info[count] = (table[i][j], (i, j))
				info_table[i][j] = count
				count += 1
	return graph_info

def check_range(x, y):
	if x < 0 or y < 0 or x >= N or y >= N:
		return False
	return True

def move_pawn(graph, info_table, num, coor):
	x, y = coor
	dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]
	for i in range(8):
		nx, ny = x + dx[i], y + dy[i]
		if not check_range(nx, ny):
			continue
		if table[nx][ny] != '0':
			graph[num].append((1, info_table[nx][ny]))

def move_knight(graph, info_table, num, coor):
	x, y = coor
	dx, dy = [-1, -2, -2, -1, 1, 2, 2, 1], [-2, -1, 1, 2, -2, -1, 1, 2]
	for i in range(8):
		nx, ny = x + dx[i], y + dy[i]
		if not check_range(nx, ny):
			continue
		if table[nx][ny] != '0':
			graph[num].append((2, info_table[nx][ny]))

def move_rook(graph, info_table, num, coor):
	x, y = coor
	count = 1
	while check_range(x + count, y):
		if table[x + count][y] != '0':
			graph[num].append((count, info_table[x + count][y]))
			break
		count += 1
	count = 1
	while check_range(x - count, y):
		if table[x - count][y] != '0':
			graph[num].append((count, info_table[x - count][y]))
			break
		count += 1
	count = 1
	while check_range(x, y + count):
		if table[x][y  + count] != '0':
			graph[num].append((count, info_table[x][y + count]))
			break
		count += 1
	count = 1
	while check_range(x, y - count):
		if table[x][y - count] != '0':
			graph[num].append((count, info_table[x][y - count]))
			break
		count += 1

def move_bishop(graph, info_table, num, coor):
	x, y = coor
	count = 1
	while check_range(x + count, y + count):
		if table[x + count][y + count] != '0':
			graph[num].append((count, info_table[x + count][y + count]))
			break
		count += 1
	count = 1
	while check_range(x - count, y - count):
		if table[x - count][y - count] != '0':
			graph[num].append((count, info_table[x - count][y - count]))
			break
		count += 1
	count = 1
	while check_range(x - count, y + count):
		if table[x - count][y  + count] != '0':
			graph[num].append((count, info_table[x - count][y + count]))
			break
		count += 1
	count = 1
	while check_range(x + count, y - count):
		if table[x + count][y - count] != '0':
			graph[num].append((count, info_table[x + count][y - count]))
			break
		count += 1
	
def init_graph(info_table):
	global start_node

	graph_info = parse_graph_info(info_table)
	graph = defaultdict(list)
	for num, info in graph_info.items():
		if info[0] == 'P':
			start_node = num
			move_pawn(graph, info_table, num, info[1])
			table[info[1][0]][info[1][1]] = '0'

	for num, info in graph_info.items():
		if info[0] == 'N':
			move_knight(graph, info_table, num, info[1])
		elif info[0] == 'R':
			move_rook(graph, info_table, num, info[1])
		elif info[0] == 'B':
			move_bishop(graph, info_table, num, info[1])
		elif info[0] == 'Q':
			move_rook(graph, info_table, num, info[1])
			move_bishop(graph, info_table, num, info[1])
	return [graph, graph_info]

def dijkstra(start, N):
	queue = []
	heapq.heappush(queue, (0, start))
	visit = [INF] * N
	visit[start] = 0
	king = -1

	while queue:
		dst, now = heapq.heappop(queue)
		if visit[now] < dst:
			continue
		if graph_info[now][0] == 'K':
			king = now
			continue
		for nxt_dst, nxt in graph[now]:
			if dst + nxt_dst >= visit[nxt]:
				continue
			visit[nxt] = dst + nxt_dst
			heapq.heappush(queue, (dst + nxt_dst, nxt))
	if king == -1:
		return -1
	return visit[king]


N = int(input())
table = [input().split() for _ in range(N)]

start_node = 0
info_table = [[-1] * N for _ in range(N)]
graph, graph_info = init_graph(info_table)
print(dijkstra(start_node, len(graph_info.keys())))
