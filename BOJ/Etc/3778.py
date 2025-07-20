n = int(input())
for i in range(1, n + 1):
    a = input().strip()
    b = input().strip()
    ca = [0] * 26
    cb = [0] * 26
    for ch in a:
        ca[ord(ch) - 97] += 1
    for ch in b:
        cb[ord(ch) - 97] += 1
    s = 0
    for j in range(26):
        s += abs(ca[j] - cb[j])
    print(f"Case #{i}: {s}")
