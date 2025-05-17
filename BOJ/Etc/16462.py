n=int(input())
t=0
for _ in range(n):
    q=input().strip()
    x=int(''.join('9' if c in '069' else c for c in q))
    if x>100: x=100
    t+=x
print((2*t+n)//(2*n))
