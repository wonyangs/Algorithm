import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = input().split()
    a = float(a)
    
    if b == 'kg':
        print("%.4f lb"%(a * 2.2046))
    elif b == 'g':
        print("%.4f l"%(a * 3.7854))
    elif b == "l":
        print("%.4f g"%(a *0.2642))
    else:
        print("%.4f kg"%(a * 0.4536))
