m = {' ': '%20', '!': '%21', '$': '%24', '%': '%25', '(': '%28', ')': '%29', '*': '%2a'}
while True:
    s = input()
    if s == '#':
        break
    r = ''
    for c in s:
        r += m.get(c, c)
    print(r)
