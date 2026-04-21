import sys
sys.set_int_max_str_digits(20000)
n, p = map(int, sys.stdin.read().split())
s = str(n ** p)
for i in range(0, len(s), 70):
    print(s[i:i+70])
