a = list(map(int, input().split()))
b = list(map(int, input().split()))

atot, btot = 0, 0
lead = 0

for i in range(9):
    atot += a[i]
    if atot > btot and lead == 0:
        lead += 1
    if atot < btot and lead == 1:
        lead += 1
    btot += b[i]

if lead == 2 and atot < btot or lead == 1 and atot < btot:
    print("Yes")
else:
    print("No")
