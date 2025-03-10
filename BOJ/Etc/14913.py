a,d,k=map(int,input().split())
if (k-a)%d!=0:
    print("X")
else:
    n=(k-a)//d+1
    if n<1:
        print("X")
    else:
        print(n)
