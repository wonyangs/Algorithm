i = 1
while True:
    s = input().split()
    if s[1] == 'E':
        break
    a, o, b = int(s[0]), s[1], int(s[2])
    r = eval(f"{a} {o} {b}")
    print(f"Case {i}: {'true' if r else 'false'}")
    i += 1
