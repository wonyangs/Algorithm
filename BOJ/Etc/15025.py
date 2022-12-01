a, b = map(int, input().split())
if a + b == 0:
    print("Not a moose")
elif a == b:
    print("Even %d"%(a * 2))
else:
    print("Odd %d"%(max(a, b) * 2))
