import sys
input = sys.stdin.readline

n, q = map(int, input().split())
s = set()
for _ in range(q):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        s.add(cmd[1])
    elif cmd[0] == 2:
        s.discard(cmd[1])
    else:
        print(n - len(s))
