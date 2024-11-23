import math

p = [i for i in range(2, 10**6+1) if all(i % d for d in range(2, int(math.sqrt(i))+1))]
for _ in range(int(input())):
    s = int(input())
    print("YES" if all(s % x for x in p if x * x <= s) else "NO")
