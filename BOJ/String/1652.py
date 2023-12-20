import sys

input = sys.stdin.readline

N = int(input())
arr = [input().strip() for _ in range(N)]

row_cnt = sum([1 for row in arr for elem in row.split('X') if len(elem) >= 2])
col_cnt = sum([1 for col in zip(*arr) for elem in ''.join(col).split('X') if len(elem) >= 2])

print(row_cnt, col_cnt)
