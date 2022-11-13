a = int(input())
b = int(input())
c = int(input())
if a+b+c != 180:
    print("Error")
elif a != b and a != c and b != c:
    print("Scalene")
elif a == 60 and b == 60:
    print("Equilateral")
else:
    print("Isosceles")
