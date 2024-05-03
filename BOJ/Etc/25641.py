N = int(input())
s = input()

t_cnt, s_cnt = s.count('t'), s.count('s')

i = 0
while t_cnt != s_cnt:
    if s[i] == 't':
        t_cnt -= 1
    else:
        s_cnt -= 1
    i += 1
print(s[i:])
