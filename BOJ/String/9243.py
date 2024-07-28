N = int(input())
a = input()
b = input()
res = True
if N % 2 == 0:
    res = a == b
else:
    for i in range(len(a)):
        if a[i] == b[i]:
            res = False
            break

print("Deletion succeeded" if res else "Deletion failed")
