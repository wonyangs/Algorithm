n = int(input())
s = [int(input()) for _ in range(n)]
print(s[-1] + (s[1] - s[0]) if s[1] - s[0] == s[2] - s[1] else s[-1] * (s[1] // s[0]))
