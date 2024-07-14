def decrypt(k, msg):
    n = len(msg)
    rows = n // k
    matrix = [[''] * k for _ in range(rows)]
    
    idx = 0
    for r in range(rows):
        if r % 2 == 0:
            for c in range(k):
                matrix[r][c] = msg[idx]
                idx += 1
        else:
            for c in range(k-1, -1, -1):
                matrix[r][c] = msg[idx]
                idx += 1
    
    return ''.join(matrix[r][c] for c in range(k) for r in range(rows))

# 예제 입력
k = int(input())
msg = input()

original = decrypt(k, msg)
print(original)
