from math import*
t=1
while s:=int(input()):
    u=int(int(s/2+.5)*1.5+.5)
    print(f"File #{t}\nJohn needs {ceil(ceil(u/62)/30000)} floppies.\n")
    t+=1
