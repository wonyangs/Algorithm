arr = [input().split() for _ in range(15)]
w, b, g = 0, 0, 0
for n in arr:
    w += n.count('w')
    b += n.count('b')
    g += n.count('g')

if w:
    print("chunbae")
elif b:
    print("nabi")
else:
    print("yeongcheol")
