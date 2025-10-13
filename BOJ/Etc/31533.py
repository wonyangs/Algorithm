a = int(input())
m, n = map(int, input().split())

t1 = min(2*m/a, 2*n, max(m/a, n))
t2 = min(2*m, 2*n/a, max(m, n/a))

print(min(t1, t2))
