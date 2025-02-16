from sys import stdin
inp = stdin.readline

sc = 0
st = [":-)", ":-(", "RIP"]

while (lst := inp().split()) != ["0", "0"]:
    base, wt = map(int, lst)
    while (cmd := inp().split()) != ["#", "0"]:
        if wt > 0:
            if cmd[0] == "F":
                wt += int(cmd[1])
            else:
                wt -= int(cmd[1])
    sc += 1
    if base * 0.5 < wt < base * 2:
        print(sc, st[0])
    elif wt <= 0:
        print(sc, st[2])
    else:
        print(sc, st[1])
