s = list(map(int, input().split()))
x = int(input())
r = s.index(x) + 1
print("A+" if r < 6 else
      "A0" if r < 16 else
      "B+" if r < 31 else
      "B0" if r < 36 else
      "C+" if r < 46 else
      "C0" if r < 49 else
      "F")
