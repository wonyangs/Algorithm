while True:
    try:
        n,w,d,t=map(int,input().split())
        e=w*(n-1)*n//2
        b=(e-t)//d
        print(b if b else n)
    except:
        break
