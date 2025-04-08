import sys
for k in sys.stdin.read().split()[1:]:
    print(int(k) * 23)
