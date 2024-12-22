import sys
N=int(sys.stdin.read())
l=["baby","sukhwan","tururu","turu","very","cute","tururu","turu","in","bed","tururu","turu","baby","sukhwan"]
r,u=(N-1)//14,(N-1)%14
if l[u][:4]=="turu":
    t=2 if l[u]=="tururu" else 1
    print(f"tu+ru*{t+r}" if t+r>=5 else "tu"+"ru"*(t+r))
else:
    print(l[u])
