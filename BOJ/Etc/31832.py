n = int(input())
for _ in range(n):
    s = input()
    if sum(c.isupper() for c in s) <= sum(c.islower() for c in s) and len(s) <= 10 and not s.isdigit():
        print(s)
        break
