t=int(input())
for i in range(1,t+1):
    b=int(input())
    s=input().strip()
    r=''
    for j in range(b):
        v=s[j*8:j*8+8].replace('I','1').replace('O','0')
        r+=chr(int(v,2))
    print(f"Case #{i}: {r}")
