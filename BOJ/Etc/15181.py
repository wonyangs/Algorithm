import sys
for s in sys.stdin.read().split():
    if s == '#':
        break
    b = 1
    for i in range(len(s) - 1):
        if (ord(s[i+1]) - ord(s[i])) % 7 not in (2, 4, 6):
            b = 0
            break
    print("That music is beautiful." if b else "Ouch! That hurts my ears.")
