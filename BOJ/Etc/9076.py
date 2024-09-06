for _ in range(int(input())):
    s = sorted(map(int, input().split()))[1:4]
    print("KIN" if s[-1] - s[0] >= 4 else sum(s))
