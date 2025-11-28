while True:
    s = input()
    if s == '#':
        break
    a = s.count('A')
    y = s.count('Y')
    n = s.count('N')
    if a >= len(s) / 2:
        print("need quorum")
    elif y > n:
        print("yes")
    elif n > y:
        print("no")
    else:
        print("tie")
