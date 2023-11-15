def hap(a, b, c):
    return a * 3 + b * 20 + c * 120

a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

a, b = hap(a1, b1, c1), hap(a2, b2, c2)
if a > b:
    print("Max")
elif a < b:
    print("Mel")
else:
    print("Draw")
