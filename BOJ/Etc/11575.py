for _ in range(int(input())):
    a, b = map(int,input().split())
    s = input().strip()
    print(''.join(chr(((a*(ord(c)-65)+b)%26)+65) for c in s))
