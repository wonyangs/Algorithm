import sys

for l in sys.stdin:
    l = l.strip()
    if l == '#': break
    
    c, t = 0, 0
    for x in l.split():
        if x == '*': break
        v = 1 if x == 'A' else int(x)
        if v % 2: c += 1
        else: t += 1
            
    if c > t: print("Cheryl")
    elif t > c: print("Tania")
    else: print("Draw")
