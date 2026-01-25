import sys
from collections import Counter, defaultdict

input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    arr = [*map(int, input().split())]
    
    count = Counter(arr)
    available_team = set([team for team, cnt in count.items() if cnt == 6])
    
    now_score = 1
    team_score = defaultdict(list)
    for team in arr:
        if team in available_team:
            team_score[team].append(now_score)
            now_score += 1
    
    min_score = min([sum(score_lst[:4]) for score_lst in team_score.values()])
    win_teams = [team for team, score in team_score.items() if sum(score[:4]) == min_score]
    
    if len(win_teams) == 1:
        print(win_teams[0])
    else:
        win_team, min_score = -1, float('inf')
        for team in win_teams:
            fifth_score = team_score[team][4]
            if fifth_score < min_score:
                min_score = fifth_score
                win_team = team
        print(win_team)
