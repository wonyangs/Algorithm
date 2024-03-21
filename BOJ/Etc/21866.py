MAX = [100, 100, 200, 200, 300, 300, 400, 400, 500]
arr = [*map(int, input().split())]

hacker = False
for i, s in enumerate(arr):
    if MAX[i] < s:
        hacker = True

if sum(arr) < 100:
    print("none")
elif hacker:
    print("hacker")
else:
    print("draw")
