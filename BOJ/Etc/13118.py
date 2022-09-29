arr = [*map(int, input().split())]
x, y, r = map(int, input().split())
try:
    print(arr.index(x)+1)
except:
    print(0)
