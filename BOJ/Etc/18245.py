i=0
while True:
    s=input()
    if s=="Was it a cat I saw?":
        break
    i+=1
    print(''.join(s[j] for j in range(0, len(s), i+1)))
