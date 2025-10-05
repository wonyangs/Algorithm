t = int(input())
for c in range(1, t+1):
    l = list(map(int, input().split()))
    n = l[0]
    r = [(n-i)*l[i+1] for i in range(n)]
    print(f"Case {c}: {n-1}", *r)
