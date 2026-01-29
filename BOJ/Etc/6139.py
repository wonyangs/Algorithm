import sys

d = sys.stdin.read().split()
n, k = int(d[0]), int(d[1])
idx = 2

for _ in range(k):
    s, t, r = int(d[idx]), int(d[idx+1]), int(d[idx+2])
    idx += 3
    
    cp = s * t
    ct = t + r
    
    if cp >= n:
        print((n + s - 1) // s)
    else:
        full = n // cp
        rem = n % cp
        
        if rem == 0:
            print(full * ct - r)
        else:
            print(full * ct + (rem + s - 1) // s)
