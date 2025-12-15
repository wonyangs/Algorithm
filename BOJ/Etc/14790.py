for t in range(1, int(input())+1):
    s = list(input())
    n = len(s)
    k = n
    for i in range(n-1, 0, -1):
        if s[i-1] > s[i]:
            s[i-1] = chr(ord(s[i-1])-1)
            k = i
    for i in range(k, n):
        s[i] = '9'
    print(f"Case #{t}: {int(''.join(s))}")
