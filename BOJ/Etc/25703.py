N = int(input())
print("int a;")
for i in range(1, N + 1):
    print("int " + "*" * i + "ptr", end="")
    if i == 1:
        print(" = &a;")
    elif i == 2:
        print("2 = &ptr;")
    else:
        print("%d = &ptr%d;"%(i, i-1))
