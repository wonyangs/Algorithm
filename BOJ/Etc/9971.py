while True:
    s = input()
    if s == "ENDOFINPUT":
        break
    if s == "START":
        m = input()
        input()
        r = ""
        for c in m:
            if c.isalpha():
                r += chr((ord(c) - 70) % 26 + 65)
            else:
                r += c
        print(r)
