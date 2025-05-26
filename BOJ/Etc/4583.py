mirror = {
    'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p',
    'i': 'i', 'o': 'o', 'v': 'v', 'w': 'w', 'x': 'x'
}
while True:
    s = input().strip()
    if s == '#':
        break
    ok = True
    res = ''
    for c in s[::-1]:
        if c in mirror:
            res += mirror[c]
        else:
            ok = False
            break
    print(res if ok else 'INVALID')
