t1, m1, t2, m2 = map(int, input().split())

start = t1 * 60 + m1
end = t2 * 60 + m2

if end < start:
    end += 24 * 60

m = end - start
n = m // 30

print(m, n)
