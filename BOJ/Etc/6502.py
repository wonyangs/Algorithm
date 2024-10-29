import math
i = 1
while (data := input().split())[0] != '0':
    r, w, l = map(int, data)
    print(f"Pizza {i} {'fits' if 2*r >= math.hypot(w, l) else 'does not fit'} on the table.")
    i += 1
