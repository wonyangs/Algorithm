n = int(input())
for _ in range(n):
    s = input()
    t = sum(ord(c) - 64 for c in s if c != ' ')
    print("PERFECT LIFE" if t == 100 else t)
