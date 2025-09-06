int(input())
a = sorted(map(int, input().split()))
print("yes" if (len(set(a)) == 1 or (len(set(a)) == 2 and a[-1] % a[0] == 0 and a.count(a[-1]) == 1)) else "no")
