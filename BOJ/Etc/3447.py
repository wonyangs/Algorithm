import sys

for line in sys.stdin:
    s = line.rstrip('\n')
    while 'BUG' in s:
        s = s.replace('BUG', '')
    print(s)
