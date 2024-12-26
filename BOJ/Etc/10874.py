p=[(i-1)%5+1 for i in range(1,11)]
N=int(input())
print(*[i+1 for i,a in enumerate([list(map(int,input().split()))for _ in range(N)])if a==p],sep='\n')
