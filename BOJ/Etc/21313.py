n = int(input())
s = [str(1 if i % 2 == 0 else 2) for i in range(n if n % 2 == 0 else n - 1)]
if n % 2:
    s.append("3")
print(" ".join(s))
