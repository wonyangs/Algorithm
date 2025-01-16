from collections import Counter
for _ in [0]*int(input()):
    c=Counter(input().replace(" ",""))
    m=max(c.values())
    print("?") if list(c.values()).count(m)>1 else print(max(c,key=c.get))
