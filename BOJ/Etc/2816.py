cList = [input() for _ in range(int(input()))]
for i in range(len(cList)):
    if cList[i] == 'KBS1':
        print('1' * i + '4' * i, end='')
        cList.insert(0, cList.pop(i))
        break
for i in range(1, len(cList)):
    if cList[i] == 'KBS2':
        print('1' * i + '4' * (i - 1), end='')
        break
