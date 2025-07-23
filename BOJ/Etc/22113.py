n, m = map(int, input().split())
b = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]
print(sum(a[b[i]-1][b[i+1]-1] for i in range(m-1)))
