t = int(input())
for _ in range(t):
    s = input()
    stripped = s.strip()
    if stripped and stripped.isdigit():
        print(int(stripped))
    else:
        print("invalid input")
