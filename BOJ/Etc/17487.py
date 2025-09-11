s = input()
left_keys = set('qwertyasdfgzxcvbQWERTYASDFGZXCVB')

l = 0
r = 0
f = 0

for c in s:
    if c == ' ':
        f += 1
    elif c.isupper():
        f += 1
        if c in left_keys:
            l += 1
        else:
            r += 1
    else:
        if c in left_keys:
            l += 1
        else:
            r += 1

min_diff = float('inf')
best = (0, 0)

for i in range(f + 1):
    lt = l + i
    rt = r + f - i
    d = abs(lt - rt)
    
    if d < min_diff:
        min_diff = d
        best = (lt, rt)
    elif d == min_diff == 1 and lt > rt:
        best = (lt, rt)

print(best[0], best[1])
