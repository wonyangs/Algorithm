t = int(input())
for i in range(1, t+1):
    l = int(input())
    k = input()
    s = input()
    c = sum(1 for j in range(l) if k[j] != s[j])
    print(f"Case {i}: {c}")
