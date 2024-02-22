import sys
input = sys.stdin.readline

n = input()

cur = 0
nxt = 0

oper = ''
res = []

for c in input():
    if c.isdigit():
        if oper:
            nxt = nxt * 10 + int(c)
        else: 
            cur = cur * 10 + int(c)
    else:
        if oper in 'SMUP':
            if oper == 'S':
                cur -= nxt
            elif oper == 'M':
                cur *= nxt
            elif oper == 'U':
                if cur < 0 and nxt != 0:
                    cur = ((cur * -1) // nxt) * -1
                elif nxt != 0:
                    cur //= nxt
            elif oper == 'P':
                cur += nxt
        if c == 'C':
            res.append(cur)
        oper = c
        nxt = 0

if not res:
    print('NO OUTPUT')
else:
    print(*res)
