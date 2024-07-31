from datetime import datetime, timedelta

f = '%H:%M:%S'
c = datetime.strptime(input().strip(), f)
s = datetime.strptime(input().strip(), f)
if c > s:
    s += timedelta(days=1)
d = s - c
print(str(d).zfill(8))
