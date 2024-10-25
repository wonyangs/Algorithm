import sys
input = sys.stdin.read

data = input().split()
N = int(data[0])
scores = [0] * N
games = [data[i:i+3] for i in range(1, len(data), 3)]

for game in range(3):
    count = {}
    for player in range(N):
        num = games[player][game]
        count[num] = count.get(num, 0) + 1
    
    for player in range(N):
        num = games[player][game]
        if count[num] == 1:
            scores[player] += int(num)

print(*scores, sep='\n')
