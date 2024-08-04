L = int(input())
s = input().strip()
r, M, h = 31, 1234567891, 0
for i in range(L):
    h += (ord(s[i]) - 96) * (r ** i)
print(h % M)
