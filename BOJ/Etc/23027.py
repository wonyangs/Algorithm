s = input().strip()
if 'A' in s:
    t, r = 'BCDF', 'A'
elif 'B' in s:
    t, r = 'CDF', 'B'
elif 'C' in s:
    t, r = 'DF', 'C'
else:
    print('A' * len(s))
    exit()
print(''.join(r if c in t else c for c in s))
