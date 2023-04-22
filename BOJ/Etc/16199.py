by, bm, bd = map(int, input().split())
cy, cm, cd = map(int, input().split())

ma = cy - by - ((cm, cd) < (bm, bd))
ca = cy - by + 1
ya = cy - by

print(ma)
print(ca)
print(ya)
