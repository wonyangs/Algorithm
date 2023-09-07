l=[elem.split() for elem in open(0).readlines()]
m=[int(elem[1])-int(elem[0]) for elem in l]
n=[sum(m[0:i]) for i in range(len(m))]
print(max(n))
