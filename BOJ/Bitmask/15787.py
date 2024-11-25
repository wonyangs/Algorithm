N, M = map(int, input().split())

train = [0] * (N + 1)
for _ in range(M):
    cmd = [*map(int, input().split())]
    if cmd[0] == 1:
        train[cmd[1]] |= 1 << (cmd[2] - 1)
    elif cmd[0] == 2:
        train[cmd[1]] &= ~(1 << (cmd[2] - 1))
    elif cmd[0] == 3:
        train[cmd[1]] <<= 1
        train[cmd[1]] &= ~(1 << 20)
    elif cmd[0] == 4:
        train[cmd[1]] >>= 1

info = set()
cnt = 0
for t in train[1:]:
    if t not in info:
        cnt += 1
        info.add(t)
print(cnt)
