t=int(input())
for _ in range(t):
    l,r,s=map(int,input().split())
    print(min(2*(r-s),2*(s-l)+1))
