def conv(arr):
    return arr[0] * 3600 + arr[1] * 60 + arr[2]


now = conv([*map(int, input().split(':'))])
nxt = conv([*map(int, input().split(':'))])

if now > nxt:
    nxt += 24 * 3600

res = nxt - now
hh = res // 3600
res %= 3600
mm = res // 60
res %= 60
ss = res
if hh == mm == ss == 0:
    print("24:00:00")
else:
    print("%02d:%02d:%02d"%(hh, mm, ss))
