N = int(input())
sp, ep = input().split('*')

for _ in range(N):
    src = input()
    if len(src) < len(sp) + len(ep):
        print("NE")
        continue
    
    if src[:len(sp)] == sp and src[-len(ep):] == ep:
        print("DA")
    else:
        print("NE")
