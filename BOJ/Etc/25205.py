n = int(input())
s = input().strip()
c = set('rsefaqtdwczxvg')
st = 0
for x in s:
    if x in c:
        st = 3 if st == 2 else 1
    else:
        st = 2
print(1 if st == 3 else 0)
