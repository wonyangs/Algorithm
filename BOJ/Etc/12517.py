t = int(input())
for i in range(1, t + 1):
    c = input().strip()
    e = c[-1]
    if e == 'y':
        r = "nobody"
    elif e in "aeiou":
        r = "a queen"
    else:
        r = "a king"
    print(f"Case #{i}: {c} is ruled by {r}.")
