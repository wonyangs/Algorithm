n = int(input())
s = input()
p = ['000000', '001111', '010011', '011100', '100110', '101001', '110101', '111010']
res = ''
for i in range(n):
    sub = s[i*6:i*6+6]
    for j in p:
        if sum(a == b for a, b in zip(sub, j)) >= 5:
            res += chr(p.index(j) + 65)
            break
    else:
        print(i + 1)
        exit()
print(res)
