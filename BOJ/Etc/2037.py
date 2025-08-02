p, w = map(int, input().split())
s = input()

d = {
    '1': [' '],
    '2': ['A', 'B', 'C'],
    '3': ['D', 'E', 'F'],
    '4': ['G', 'H', 'I'],
    '5': ['J', 'K', 'L'],
    '6': ['M', 'N', 'O'],
    '7': ['P', 'Q', 'R', 'S'],
    '8': ['T', 'U', 'V'],
    '9': ['W', 'X', 'Y', 'Z']
}

mp = {}
for k, v in d.items():
    for i, ch in enumerate(v):
        mp[ch] = (k, i + 1)

t = 0
prev_btn = ''
for c in s:
    btn, cnt = mp[c]
    if prev_btn == btn and c != ' ':
        t += w
    t += p * cnt
    prev_btn = btn

print(t)
