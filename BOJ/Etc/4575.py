import sys

for s in sys.stdin:
    s = s.rstrip('\n')
    if s == "END":
        break
    t = s.replace(" ", "")
    if len(t) == len(set(t)):
        print(s)
