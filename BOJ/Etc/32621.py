try:
    s = input().split('+')
    if len(s) == 2 and s[0] == s[1] and s[0].isdigit() and s[0][0] != '0':
        print("CUTE")
    else:
        print("No Money")
except:
    print("No Money")
