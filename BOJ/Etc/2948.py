import datetime
D, M = map(int, input().split())
print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][datetime.date(2009, M, D).weekday()])
