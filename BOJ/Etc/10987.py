s = input()
m = 'aeiou'
count = 0
for c in s:
    if c in m:
        count += 1
print(count)
