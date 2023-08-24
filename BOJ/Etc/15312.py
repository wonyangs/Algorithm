num = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

a = input()
b = input()

arr = []

for i in range(len(a)):
    n, m = a[i], b[i]
    arr.append(num[ord(n) - ord('A')])
    arr.append(num[ord(m) - ord('A')])

while len(arr) != 2:
    arr = [(arr[i] + arr[i + 1]) % 10 for i in range(len(arr) - 1)]
print(*arr, sep='')
