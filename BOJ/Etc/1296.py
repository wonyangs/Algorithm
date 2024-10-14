yeondoo = input().strip()
teams = [input().strip() for _ in range(int(input().strip()))]
print(min(teams, key=lambda t: (-((lambda n:((n.count('L')+n.count('O'))*(n.count('L')+n.count('V'))*(n.count('L')+n.count('E'))*(n.count('O')+n.count('V'))*(n.count('O')+n.count('E'))*(n.count('V')+n.count('E'))) % 100)(yeondoo+t)), t)))
