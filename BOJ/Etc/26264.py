N = int(input())
s = input()
a, b = s.count('b'), s.count('s')
if a > b:
    print("bigdata?")
elif a < b:
    print("security!")
else:
    print("bigdata? security!")
