A, B = input().split()

def diff(x, y):
    cnt = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            cnt += 1
    return cnt
    
MAX = 1e9
for i in range(len(B) - len(A) + 1):
    MAX = min(MAX, diff(A, B[i:len(A)+i]))
print(MAX)
