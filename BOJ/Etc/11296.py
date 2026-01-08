N = int(input())
D = {'R': 0.55, 'G': 0.70, 'B': 0.80, 'Y': 0.85, 'O': 0.90, 'W': 0.95}

for _ in range(N):
    L = input().split()
    P = float(L[0])
    V = P * D[L[1]]

    if L[2] == 'C':
        V *= 0.95

    if L[3] == 'P':
        ans = int(V * 100 + 0.5) / 100
    else:
        ans = int(V * 10 + 0.4) / 10

    print("$%.2f" % ans)
