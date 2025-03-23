d = {'S': 'P', 'R': 'S', 'P': 'R'}
ml, mr, tl, tr = input().split()

m_win = (d[ml] == tl and d[ml] == tr) or (d[mr] == tl and d[mr] == tr)
t_win = (d[tl] == ml and d[tl] == mr) or (d[tr] == ml and d[tr] == mr)

if m_win:
    print('MS')
elif t_win:
    print('TK')
else:
    print('?')
