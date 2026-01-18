import sys

input = sys.stdin.readline

mode_count_dict = {'Y': 2, 'F': 3, 'O': 4}

M, mode = input().split()
M = int(M)

name_set = set()
for _ in range(M):
    name = input().strip()
    name_set.add(name)

print(len(name_set) // (mode_count_dict[mode] - 1))
