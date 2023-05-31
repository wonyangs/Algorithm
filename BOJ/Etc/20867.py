M, S, G = map(float, input().split())
A, B = map(float, input().split())
L, R = map(float, input().split())
print('friskus' if L / A + M / G < R / B + M / S else 'latmask')
