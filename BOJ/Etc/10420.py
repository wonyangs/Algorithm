from datetime import date, timedelta
n = int(input())
d = date(2014, 4, 2) + timedelta(days=n-1)
print(d.strftime("%Y-%m-%d"))
