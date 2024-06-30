from collections import defaultdict

dic = defaultdict(int)
try:
    while True:
        for c in input():
            if c != ' ':
                dic[c] += 1
except:
    arr = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
    for c in arr:
        if c[1] == arr[0][1]:
            print(c[0], end='')
    print()
