flag = False
cnt = 2
res = 2
for _ in range(int(input()) - 1):
    res += cnt
    if flag is False:
        flag = True
    else:
        cnt += 1
        flag = False
print(res)
