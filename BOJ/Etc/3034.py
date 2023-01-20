N, W, H = map(int, input().split())
a = (W**2 + H **2)**0.5
for _ in range(N):
    if int(input()) <= a:
        print("DA")
    else:
        print("NE")
