n = int(input())
s = input()

r = ''.join(c for c in s if c not in 'JAV')

print(r if r else 'nojava')
