# Solved on 2022.07.28
# 5597 과제 안 내신 분..?

s = set(i for i in range(1, 31))
for _ in range(28):
    s.remove(int(input()))
print(*sorted(s), sep='\n')
