for _ in range(int(input())):
    a, b = input().split()
    b = int(b)
    if 97 <= b <= 100:
        b = 'A+'
    elif 90 <= b <= 96:
        b = 'A'
    elif 87 <= b <= 89:
        b = 'B+'
    elif 80 <= b <= 86:
        b = 'B'
    elif 77 <= b <= 79:
        b = 'C+'
    elif 70 <= b <= 76:
        b = 'C'
    elif 67 <= b <= 69:
        b = 'D+'
    elif 60 <= b <= 66:
        b = 'D'
    else:
        b = 'F'
    print(a, b)
