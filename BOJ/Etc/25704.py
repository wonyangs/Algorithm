N = int(input())
P = int(input())

arr = [P]

if N >= 20:
    arr.append(P * 0.75)
if N >= 15:
    arr.append(P - 2000)
if N >= 10:
    arr.append(P * 0.9)
if N >= 5:
    arr.append(P - 500)

print(max(0, int(min(arr))))
