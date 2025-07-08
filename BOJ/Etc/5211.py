s = input().strip()
ms = s.split('|')
n = m = 0
for x in ms:
    f = x[0]
    if f in 'ADE':
        n += 1
    elif f in 'CFG':
        m += 1
if n > m:
    print('A-minor')
elif m > n:
    print('C-major')
else:
    l = s[-1]
    if l in 'ADE':
        print('A-minor')
    else:
        print('C-major')
