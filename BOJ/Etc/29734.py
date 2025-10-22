N, M = map(int, input().split())
T, S = map(int, input().split())

h = N + (N-1)//8 * S
d = T + M + (M-1)//8 * (2*T+S)

if h < d:
    print("Zip")
    print(h)
else:
    print("Dok")
    print(d)
