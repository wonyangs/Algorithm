while True:
    try:
        s = input()
    except:
        break
    if s == '#': break
    u, v, w = s.split()
    r = ''
    for i in range(len(u)):
        c = (ord(w[i]) - 97 + ord(v[i]) - ord(u[i])) % 26
        r += chr(c + 97)
    print(u, v, w, r)
