import sys
input = sys.stdin.readline

for _ in range(int(input())):
    print(''.join(' ' if (v := sum(ord(c) - 97 for c in w) % 27) == 26 else chr(97 + v) for w in input().split()))
