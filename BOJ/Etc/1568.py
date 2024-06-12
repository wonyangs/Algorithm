N = int(input())

now = 1
cnt = 0
while N:
    if now <= N:
        N -= now
    else:
        now = 1
        N -= now
    now += 1
    cnt += 1
print(cnt)
