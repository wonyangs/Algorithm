w={}
st={}
while 1:
    d=input().split()
    if d[0]=='-1': break
    t=int(d[0]); p=d[1]; r=d[2]
    if p in st: continue
    if r=='wrong': w[p]=w.get(p,0)+1
    else: st[p]=t
n=len(st)
pen=0
for k,v in st.items():
    pen+=v+w.get(k,0)*20
print(n,pen)
