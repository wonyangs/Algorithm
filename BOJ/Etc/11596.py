a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()))

if a == b and a[0]**2 + a[1]**2 == a[2]**2:
    print("YES")
else:
    print("NO")
