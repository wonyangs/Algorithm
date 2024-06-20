import sys
input = sys.stdin.readline

while True:
    arr = input().strip().split()
    
    c = arr[0]
    if c == '#':
        break
    s = ''.join(arr[1:])
    print(c, s.count(c) + s.count(c.upper()))
