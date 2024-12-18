n = int(input())
s = input()
result = ""
for i in range(n):
    if s[i] == 'l':
        result += 'L'
    else:
        result += 'i'
print(result)
