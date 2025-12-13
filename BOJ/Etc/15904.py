s = input()
t = "UCPC"
j = 0
for c in s:
    if j < 4 and c == t[j]:
        j += 1
print("I love UCPC" if j == 4 else "I hate UCPC")
