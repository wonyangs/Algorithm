input()
s=sum([*map(int,input().split())])
if s > 0:
    print("Right")
elif s == 0:
    print("Stay")
else:
    print("Left")
