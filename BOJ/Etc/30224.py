N = input()
if N.count('7') == 0 and int(N) % 7 != 0:
    print(0)
elif N.count('7') == 0 and int(N) % 7 == 0:
    print(1)
elif N.count('7') != 0 and int(N) % 7 != 0:
    print(2)
else:
    print(3)
