d = {
    'A': 'a',
    'B': 'b',
    'E': 'ye',
    'K': 'k',
    'M': 'm',
    'H': 'n',
    'O': 'o',
    'P': 'r',
    'C': 's',
    'T': 't',
    'Y': 'u',
    'X': 'h'
}

s = input()
r = ''
for c in s:
    if c == 'B':
        r += 'v'
    elif c == 'E':
        r += 'ye'
    elif c == 'H':
        r += 'n'
    elif c == 'P':
        r += 'r'
    elif c == 'C':
        r += 's'
    elif c == 'Y':
        r += 'u'
    elif c == 'X':
        r += 'h'
    else:
        r += c.lower()
print(r)
