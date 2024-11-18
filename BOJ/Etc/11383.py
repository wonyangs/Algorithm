N, M = map(int, input().split())
o = [input() for _ in range(N)]
s = [input() for _ in range(N)]
print("Eyfa" if all(''.join(c*2 for c in o[i]) == s[i] for i in range(N)) else "Not Eyfa")
