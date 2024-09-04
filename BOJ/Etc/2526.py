def f(N,P):
    s,c=[],N
    while c not in s:s.append(c);c=c*N%P
    return len(s[s.index(c):])

N,P=map(int,input().split())
print(f(N,P))
