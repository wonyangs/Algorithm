for _ in range(int(input())):
    a, b = 0, 0
    for __ in range(int(input())):
        p1, p2 = input().split()
        
        if p1 == 'R':
            if p2 == 'S':
                a += 1
            elif p2 == 'P':
                b += 1
        elif p1 == 'S':
            if p2 == 'P':
                a += 1
            elif p2 == 'R':
                b += 1
        elif p1 == 'P':
            if p2 == 'R':
                a += 1
            elif p2 == 'S':
                b += 1
        
    if a > b:
        print("Player 1")
    elif a < b:
        print("Player 2")
    else:
        print("TIE")
