n=int(input())
s=input().strip()
i=0
c=0
while i<n-3:
    if s[i]=='p' and s[i+1]=='P' and s[i+2]=='A' and s[i+3]=='p':
        c+=1
        i+=4
    else:
        i+=1
print(c)
