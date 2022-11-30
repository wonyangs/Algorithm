N = int(input())
cnt = 0
for _ in range(N):
    d = input()
    if int(d[2:]) <= 90:
        cnt += 1
print(cnt)
