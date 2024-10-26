text = input().strip()
i, result = 0, []

while i < len(text):
    result.append(text[i])
    i += 3 if text[i] in "aeiou" and i + 2 < len(text) and text[i + 1] == 'p' and text[i + 2] == text[i] else 1

print(''.join(result))
