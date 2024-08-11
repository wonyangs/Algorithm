import sys

input = sys.stdin.readline

while True:
    s = input().strip().lower()
    if s == "#":
        break
    t = set()
    for c in s:
        if c.isalpha():
            t.add(c)
    
    print(len(t))
