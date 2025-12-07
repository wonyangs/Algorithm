s = input().upper()
for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    print(c, "|", "*" * s.count(c))
