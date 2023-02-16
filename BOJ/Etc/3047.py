lst = [*map(int, input().split())]
lst.sort()
s = input()
cnt = 0
for c in s:
    if c == 'A':
        print(lst[0], end='')
    elif c == 'B':
        print(lst[1], end='')
    else:
        print(lst[2], end='')
    cnt += 1
    if cnt != 3:
        print(' ', end='')
    else:
        print()
