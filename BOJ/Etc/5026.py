import sys
input = sys.stdin.readline
for _ in range(int(input())):
    s = input().strip()
    if s == "P=NP":
        print("skipped")
        continue
    a, b = map(int, s.split('+'))
    print(a + b)
