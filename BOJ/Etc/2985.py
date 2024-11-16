a, b, c = map(int, input().split())
print(f"{a}+{b}={c}" if a+b==c else f"{a}-{b}={c}" if a-b==c else f"{a}*{b}={c}" if a*b==c else f"{a}/{b}={c}" if a/b==c else f"{a}={b}+{c}" if a==b+c else f"{a}={b}-{c}" if a==b-c else f"{a}={b}*{c}" if a==b*c else f"{a}={b}/{c}")
