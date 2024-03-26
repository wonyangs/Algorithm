K = int(input())
N = int(input())
ans = [input().split() for _ in range(N)]
time = 210
now = K - 1
for t, status in ans:
    t = int(t)
    if time - t <= 0:
        print(now+1)
        break
    time -= t
    if status == 'T':
        now = (now + 1) % 8
