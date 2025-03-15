n, p = map(int, input().split())
ans = 1
for i in range(2, n+1):
    ans = (ans*i)%p
print(ans%p)
