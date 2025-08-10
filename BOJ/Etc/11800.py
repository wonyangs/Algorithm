t = int(input())
s = ['Yakk', 'Doh', 'Seh', 'Ghar', 'Bang', 'Sheesh']
d = {1: 'Habb Yakk', 2: 'Dobara', 3: 'Dousa', 4: 'Dorgy', 5: 'Dabash', 6: 'Dosh'}
for i in range(1, t + 1):
    a, b = map(int, input().split())
    if a < b:
        a, b = b, a
    if a == b:
        r = d[a]
    elif a == 6 and b == 5:
        r = 'Sheesh Beesh'
    else:
        r = f'{s[a-1]} {s[b-1]}'
    print(f'Case {i}: {r}')
