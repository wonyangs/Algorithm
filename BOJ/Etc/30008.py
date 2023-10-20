N, K = map(int, input().split())
G = list(map(int, input().split()))

grades = [(4, 1), (11, 2), (23, 3), (40, 4), (60, 5), (77, 6), (89, 7), (96, 8), (100 ,9)]

for g in G:
    P = g * 100 // N

    for grade in grades:
        if P <= grade[0]:
            print(grade[1], end=' ')
            break

print()
