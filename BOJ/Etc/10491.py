import sys
for l in sys.stdin:
    print('yes' if 'problem' in l.lower() else 'no')
