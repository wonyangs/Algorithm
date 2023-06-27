n = int(input())
for _ in range(n):
    w, h, f = map(int, input().split())
    print("Data set:", w, h, f)
    for _ in range(f):
        if w > h:
            w //= 2
        else:
            h //= 2
    print(max(w, h), min(w, h), "\n")
