N = input()
print("YES" if any(eval('*'.join(N[:i])) == eval('*'.join(N[i:])) for i in range(1, len(N))) else "NO")
