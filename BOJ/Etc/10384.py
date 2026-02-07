import sys

n = int(sys.stdin.readline())

for i in range(1, n + 1):
    s = sys.stdin.readline().lower()
    m = min(s.count(chr(c)) for c in range(97, 123))

    if m >= 3:
        r = "Triple pangram!!!"
    elif m == 2:
        r = "Double pangram!!"
    elif m == 1:
        r = "Pangram!"
    else:
        r = "Not a pangram"

    print(f"Case {i}: {r}")
