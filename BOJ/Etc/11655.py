s = input()
result = []

for c in s:
    if 'a' <= c <= 'z':
        result.append(chr((ord(c) - ord('a') + 13) % 26 + ord('a')))
    elif 'A' <= c <= 'Z':
        result.append(chr((ord(c) - ord('A') + 13) % 26 + ord('A')))
    else:
        result.append(c)

print("".join(result))
