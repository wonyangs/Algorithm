arrA = [int(input()) for _ in range(4)]
arrB = [int(input()) for _ in range(2)]
arrA.sort()
arrB.sort()
print(sum(arrA[1:])+arrB[1])
