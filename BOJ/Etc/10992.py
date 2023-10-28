N = int(input())

for i in range(N):
    if i == N-1:
        print('*' * ((N*2)-1))
    else:
        print(' ' * (N-i-1) + '*' + ' ' * (2*i-1) + '*' * (i != 0))
