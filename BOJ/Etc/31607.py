a = int(input())
b = int(input())
c = int(input())
print(1 if a == b + c or b == a + c or c == a + b else 0)
