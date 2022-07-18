# Solved on 2022. 7. 19.
# 2744 대소문자 바꾸기

import sys
input = sys.stdin.readline

str = input().strip()
diff = ord('a') - ord('A')
for c in str:
    if c.islower():
        print(chr(ord(c) - diff), end='')
    else:
        print(chr(ord(c) + diff), end='')
print()
