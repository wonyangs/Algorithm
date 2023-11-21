N = int(input())

while True:
    if N == 1:
        print(1)
        break
    
    if N % 2 == 0:
        N //= 2
    else:
        print(0)
        break
