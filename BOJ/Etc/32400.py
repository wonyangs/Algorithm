d = list(map(int, input().split()))
idx = d.index(20)
a = (20 + d[(idx-1)%20] + d[(idx+1)%20]) / 3
b = sum(d) / 20
if a > b:
    print("Alice")
elif b > a:
    print("Bob")
else:
    print("Tie")
