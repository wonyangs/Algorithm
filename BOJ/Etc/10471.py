w, p = map(int, input().split())
pos = [0] + list(map(int, input().split())) + [w]

s = set()
for i in range(len(pos)):
    for j in range(i + 1, len(pos)):
        s.add(pos[j] - pos[i])

print(' '.join(map(str, sorted(s))))
