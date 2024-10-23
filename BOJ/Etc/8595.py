n = int(input())
s = input()
temp = ''
total = 0

for ch in s:
    if '0' <= ch <= '9':
        temp += ch
    elif temp != '':
        total += int(temp)
        temp = ''
if temp != '':
    total += int(temp)

print(total)
