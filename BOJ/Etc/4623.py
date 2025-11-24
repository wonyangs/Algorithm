while True:
    a,b,c,d = map(int,input().split())
    if a==0: break
    if (a<=c and b<=d) or (b<=c and a<=d):
        print("100%")
    else:
        r = max(min(c/a,d/b), min(c/b,d/a))
        print(f"{int(r*100)}%")
