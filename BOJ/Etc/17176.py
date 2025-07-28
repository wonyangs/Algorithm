from collections import Counter
n = int(input())
a = list(map(int, input().split()))
s = input()
m = Counter(a)
c = Counter((0 if t == ' ' else ord(t) - 64 if t < '[' else ord(t) - 70) for t in s)
print('y' if m == c else 'n')
