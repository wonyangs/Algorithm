arr = [int(input()) for _ in range(6)]
apple = arr[0] + sum(arr[:2]) + sum(arr[:3])
banana = arr[3] + sum(arr[3:5]) + sum(arr[3:])
if apple > banana:
    print('A')
elif apple < banana:
    print('B')
else:
    print('T')
