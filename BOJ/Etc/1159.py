from collections import Counter

n = int(input())
players = [input().strip()[0] for _ in range(n)]

counter = Counter(players)

result = sorted([letter for letter, count in counter.items() if count >= 5])

if result:
    print(''.join(result))
else:
    print("PREDAJA")
