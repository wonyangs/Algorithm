N, S = int(input()), input()
score = bonus = 0
for i, c in enumerate(S, 1):
    if c == 'O':
        score += i + bonus
        bonus += 1
    else:
        bonus = 0
print(score)
