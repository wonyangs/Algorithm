N = int(input())
S = input().strip()
m = set('aeiou')
count = 0
for c in S:
    if c in m:
        count += 1
print(count)
