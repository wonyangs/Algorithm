input()
s = input().split()
print(1 if all(w[0] == s[0][0] for w in s) else 0)
