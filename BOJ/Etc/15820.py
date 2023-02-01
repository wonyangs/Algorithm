a, b = map(int, input().split())
resa, resb = True, True
for _ in range(a):
    x, y = map(int, input().split())
    if x != y:
        resa = False
for _ in range(b):
    x, y = map(int, input().split())
    if x != y:
        resb = False
if resa and resb:
    print("Accepted")
elif resa and resb is False:
    print("Why Wrong!!!")
else:
    print("Wrong Answer")
