# Solved on 2022. 3. 27.
# 7785 회사에 있는 사람

import sys
input = sys.stdin.readline

N = int(input())

member = set()
for _ in range(N):
    name, cmd = input().split()
    if cmd == 'enter':
        member.add(name)
    else:
        member.remove(name)

for n in sorted(member, reverse = True):
    print(n)
