f = {'l': False, 'k': False, 'p': False}
flag = True
for _ in range(3):
    s = input()
    if s[0] in f.keys():
        f[s[0]] = True

print("GLOBAL" if f['l'] & f['k'] & f['p'] else "PONIX")
