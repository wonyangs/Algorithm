k=int(input())
p={(i+1):(i//3,i%3)for i in range(9)}
g=[[j*3+i+1 for i in range(3)]for j in range(3)]
v=[0]*10
v[k]=1
def f(c,n):
 if n==9:return 1
 r,c=p[c]
 t=0
 for d in[(0,1),(0,-1),(1,0),(-1,0)]:
  x,y=r+d[0],c+d[1]
  if 0<=x<3 and 0<=y<3 and not v[g[x][y]]:
   v[g[x][y]]=1
   t+=f(g[x][y],n+1)
   v[g[x][y]]=0
 return t
print(f(k,1))
