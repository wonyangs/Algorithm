n=int(input())
a=int(input())
if n>5:
    print("Love is open door")
else:
    for i in range(2,n+1):
        print(a if i%2 else 1-a)
