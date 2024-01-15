x,y = map(int, input().split())
print(["SUN","MON","TUE","WED","THU","FRI","SAT"][(sum([0,31,28,31,30,31,30,31,31,30,31,30,31][:x])+y)%7])
