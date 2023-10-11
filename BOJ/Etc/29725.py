scores = {'K': 0, 'k': 0,
                'P': 1, 'p': -1,
                'N': 3, 'n': -3,
                'B': 3, 'b': -3,
                'R': 5, 'r': -5,
                'Q': 9, 'q': -9}

score = 0
for _ in range(8):
    row = input()
    for p in row:
        score += scores.get(p, 0)

print(score)
