p = input()
r, l, d = 1, 26, 10

for i in range(len(p)):
    if p[i] == 'c':
        r *= l if i == 0 or p[i-1] != 'c' else l - 1
    else:
        r *= d if i == 0 or p[i-1] != 'd' else d - 1

print(r)
