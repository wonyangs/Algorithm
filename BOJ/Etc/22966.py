arr = []
for n in range(int(input())):
    a, b = input().split()
    arr.append((a, int(b)))
    
arr.sort(key=lambda x: x[1])
print(arr[0][0])
