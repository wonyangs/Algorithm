w = int(input().strip())
l = int(input().strip())
h = int(input().strip())

short, long = sorted([w, l])

if short / h >= 2 and long / short <= 2:
    print("good")
else:
    print("bad")
