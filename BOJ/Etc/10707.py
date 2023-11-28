def X():
    return A * P

def Y():
    if P < C:
        return B
    else:
        return B + (P - C) * D

arr = [int(input()) for _ in range(5)]
A, B, C, D, P = arr

print(min(X(), Y()))
