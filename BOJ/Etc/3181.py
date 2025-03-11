import sys

s = sys.stdin.read().strip()
ws = s.split(" ")
ig = {'i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili'}
res = []

for i, w in enumerate(ws) :
    if i == 0 or w not in ig :
        res.append(w[0])

print("".join(res).upper())
