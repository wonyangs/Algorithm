def p(s):
    v = "aeiou"
    if s[0] in v:
        return s + "ay"
    for i, c in enumerate(s):
        if c in v:
            return s[i:] + s[:i] + "ay"
    return s + "ay"


while True:
    w = input().strip()
    if w == "#":
        break
    print(p(w))
