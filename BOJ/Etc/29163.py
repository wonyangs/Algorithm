N = int(input())
arr = [*map(int, input().split())]

even, odd = 0, 0
for n in arr:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
if even > odd:
    print("Happy")
else:
    print("Sad")
