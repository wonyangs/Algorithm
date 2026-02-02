import sys

def p(s):
    a, b = map(int, s[:-1].split("'"))
    return a * 12 + b

def f(n):
    return f"{n // 12}'{n % 12}\""

t = int(sys.stdin.readline())
for i in range(1, t + 1):
    l = sys.stdin.readline().split()
    g = l[0]
    m, d = p(l[1]), p(l[2])
    
    v = m + d + (5 if g == 'B' else -5)
    
    mn = (v - 7) // 2
    mx = (v + 8) // 2
    
    print(f"Case #{i}: {f(mn)} to {f(mx)}")
