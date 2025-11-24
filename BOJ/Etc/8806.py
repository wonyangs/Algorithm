z = int(input())
for _ in range(z):
    x1, y1, z1 = map(float, input().split())
    x2, y2, z2 = map(float, input().split())
    
    a = x1*y2 + y1*z2 + z1*x2
    g = x2*y1 + y2*z1 + z2*x1
    
    if abs(a - g) < 1e-9:
        print("=")
    elif a > g:
        print("ADAM")
    else:
        print("GOSIA")
