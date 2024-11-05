R, C, ZR, ZC = map(int, input().split())
for row in [input().strip() for _ in range(R)]:
    e = ''.join(char * ZC for char in row)
    print((e + '\n') * ZR, end='')
