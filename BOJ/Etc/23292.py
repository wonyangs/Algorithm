b = input()
n = int(input())
dates = [input() for _ in range(n)]

by, bm, bd = b[:4], b[4:6], b[6:8]
mx = -1
ans = "99999999"

for d in dates:
    cy, cm, cd = d[:4], d[4:6], d[6:8]
    
    ys = sum((int(by[i])-int(cy[i]))**2 for i in range(4))
    ms = sum((int(bm[i])-int(cm[i]))**2 for i in range(2))
    ds = sum((int(bd[i])-int(cd[i]))**2 for i in range(2))
    
    v = ys * ms * ds
    
    if v > mx or (v == mx and d < ans):
        mx, ans = v, d

print(ans)
