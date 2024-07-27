import sys

while True:
    try:
        l = input()
        lc = sum(1 for c in l if c.islower())
        uc = sum(1 for c in l if c.isupper())
        d = sum(1 for c in l if c.isdigit())
        s = sum(1 for c in l if c.isspace())
        print(lc, uc, d, s)
    except EOFError:
        break
