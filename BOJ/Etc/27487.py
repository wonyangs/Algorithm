import sys

d = sys.stdin.read().split()
it = iter(d)
t = int(next(it))

for _ in range(t):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    
    c = a.count(2)
    
    if c == 0:
        print(1)
        continue
        
    if c % 2 != 0:
        print(-1)
        continue
        
    tgt = c // 2
    cur = 0
    
    for i, x in enumerate(a):
        if x == 2:
            cur += 1
        if cur == tgt:
            print(i + 1)
            break
