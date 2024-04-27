for _ in range(3):
    s = input()
    MAX = 1
    cnt = 1
    for i in range(7):
        if s[i] == s[i+1]:
            cnt += 1
        else:
            MAX = max(MAX, cnt)
            cnt = 1
    MAX = max(MAX, cnt)
    print(MAX)
