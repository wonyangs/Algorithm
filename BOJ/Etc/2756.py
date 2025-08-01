t = int(input())
for _ in range(t):
    a = list(map(float, input().split()))
    s1 = 0
    for i in range(0, 6, 2):
        x = a[i]
        y = a[i+1]
        d2 = x*x + y*y
        if d2 <= 9:
            s1 += 100
        elif d2 <= 36:
            s1 += 80
        elif d2 <= 81:
            s1 += 60
        elif d2 <= 144:
            s1 += 40
        elif d2 <= 225:
            s1 += 20
    s2 = 0
    for i in range(6, 12, 2):
        x = a[i]
        y = a[i+1]
        d2 = x*x + y*y
        if d2 <= 9:
            s2 += 100
        elif d2 <= 36:
            s2 += 80
        elif d2 <= 81:
            s2 += 60
        elif d2 <= 144:
            s2 += 40
        elif d2 <= 225:
            s2 += 20
    if s1 > s2:
        print(f"SCORE: {s1} to {s2}, PLAYER 1 WINS.")
    elif s2 > s1:
        print(f"SCORE: {s1} to {s2}, PLAYER 2 WINS.")
    else:
        print(f"SCORE: {s1} to {s2}, TIE.")
