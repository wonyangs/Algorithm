t = int(input())

for _ in range(t):
    n = int(input())
    r = 0
    p = float('inf')
    
    for _ in range(n):
        w, c = map(int, input().split())
        ratio = w / c
        
        if ratio > r or (ratio == r and c < p):
            r = ratio
            p = c
    
    print(p)
