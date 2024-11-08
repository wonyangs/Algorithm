m = {'-': 0, '\\': 1, '(': 2, '@': 3, '?': 4, '>': 5, '&': 6, '%': 7, '/': -1}
while (s := input().strip()) != '#':
    print(sum(m[c] * 8 ** i for i, c in enumerate(s[::-1])))
