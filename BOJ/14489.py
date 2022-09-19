a, b = map(int, input().split())
c = int(input())
print((a+b)-2*c if 2*c <= a+b else a+b)
