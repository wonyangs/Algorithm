import sys
m = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
for r in sys.stdin:
    r = r.strip()
    if r == "0 #":
        break
    if not r:
        continue
    d, mo = r.split()
    if d == "29" and mo == "February":
        print("Unlucky")
    else:
        v = (m.index(mo), int(d))
        if v < (8, 4):
            print("Yes")
        elif v > (8, 4):
            print("No")
        else:
            print("Happy birthday")
