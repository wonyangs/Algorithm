h1,h2=map(int,input().split())
d=12*h1-h2
if d%360==0 and 0<=d//360<=11:
    print('O')
else:
    print('X')
