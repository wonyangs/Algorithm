for _ in range(int(input())):
    s = input()
    a, b = s[len(s)//2-1], s[len(s)//2]
    print("Do-it" if a == b else "Do-it-Not")
