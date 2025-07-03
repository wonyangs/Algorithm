n,m=map(int,input().split())
a=[int(input()) for _ in range(n-1)]
b=list(map(int,input().split()))
for r in range(1,n+1):
    for c in range(1,m+1):
        ok=True
        for i,v in enumerate(a,1):
            if abs(r-i)+abs(c-1)!=v:
                ok=False
                break
        if not ok:
            continue
        for j,w in enumerate(b,1):
            if abs(r-n)+abs(c-j)!=w:
                ok=False
                break
        if ok:
            print(r,c)
            exit()
