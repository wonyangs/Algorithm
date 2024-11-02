n, answers = int(input()), input().strip()
patterns = {"Adrian": "ABC", "Bruno": "BABC", "Goran": "CCAABB"}
scores = {k: sum(answers[i] == v[i % len(v)] for i in range(n)) for k, v in patterns.items()}
max_score = max(scores.values())
print(max_score, *sorted([k for k, v in scores.items() if v == max_score]), sep='\n')
