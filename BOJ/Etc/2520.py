t = int(input())
for _ in range(t):
    input()
    cm, y, ssu, ssa, f = map(int, input().split())
    b, gs, gc, w = map(int, input().split())
    
    d = min(cm * 16 // 8, y * 16 // 8, ssu * 16 // 4, ssa * 16 // 1, f * 16 // 9)
    p = b + gs // 30 + gc // 25 + w // 10
    
    print(min(d, p))
