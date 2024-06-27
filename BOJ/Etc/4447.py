import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().strip()
    t = s.lower()
    
    a, b = t.count('b'), t.count('g')
    if a < b:
        print(f'{s} is GOOD')
    elif a == b:
        print(f'{s} is NEUTRAL')
    else:
        print(f'{s} is A BADDY')
