while True:
    p1 = input()
    if p1 == 'E':
        break
    p2 = input()
    
    w1 = 0
    w2 = 0
    
    for a, b in zip(p1, p2):
        if a == b:
            continue
        if (a == 'R' and b == 'S') or (a == 'P' and b == 'R') or (a == 'S' and b == 'P'):
            w1 += 1
        else:
            w2 += 1
    
    print(f"P1: {w1}")
    print(f"P2: {w2}")
