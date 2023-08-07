arr = [int(input()) for _ in range(5)]
for c in arr:
    if arr.count(c) % 2 != 0:
        print(c)
        break
