arr = list(map(int, input().split()))
name = 'ABC'
hap = sum(arr)
if hap == 0 or hap == 3:
    print("*")
elif hap == 1:
    print(name[arr.index(1)])
elif hap == 2:
    print(name[arr.index(0)])
