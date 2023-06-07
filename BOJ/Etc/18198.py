s = input()
score = {'A': 0, 'B': 0}
winner = None
final = False

for i in range(0, len(s), 2):
    player = s[i]
    points = int(s[i+1])
    score[player] += points
    
    if score['A'] == score['B'] == 10:
        final = True
    if final is True and abs(score['A'] - score['B']) >= 2:
        winner = player
        break
    if final is False and score[player] >= 11:
        winner = player
        break

print(winner)
