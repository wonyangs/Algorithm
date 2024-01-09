arr = [2**i for i in range(1, 30)]
aarr = [0]
for i in range(len(arr)):
    aarr.append(aarr[-1] + arr[i])

N = int(input())
digit = 1
while True:
    if aarr[digit - 1] < N <= aarr[digit]:
        break
    digit += 1
res = N - aarr[digit - 1]

result = ['4' if n == '0' else '7' for n in bin(res - 1)[2:].zfill(digit)]
print(''.join(result))
