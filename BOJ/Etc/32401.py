n = int(input())
s = input()
c = 0
for i in range(n-2):
    for j in range(i+2, n):
        t = s[i:j+1]
        if t[0] == 'A' and t[-1] == 'A' and t[1:-1].count('A') == 0 and t.count('N') == 1:
            c += 1
print(c)
