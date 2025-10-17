n = int(input())
a, b, c, d = map(int, input().split())
s = input()

if s[0] != 'a' or s[-1] != 'a':
    print("No")
    exit()

for i in range(1, n):
    if s[i] == s[i-1]:
        print("No")
        exit()

ca = s.count('a')
cb = s.count('b')
cc = s.count('c')
cd = s.count('d')

if ca <= a and cb <= b and cc <= c and cd <= d:
    print("Yes")
else:
    print("No")
