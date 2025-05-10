from collections import Counter

i = 1
while True:
    a = input()
    b = input()
    if a == 'END' and b == 'END':
        break
    print(f"Case {i}: {'same' if Counter(a) == Counter(b) else 'different'}")
    i += 1
