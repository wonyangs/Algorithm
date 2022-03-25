# Solved on 2022. 3. 26.
# 1475 방 번호

from collections import Counter
import sys
input = sys.stdin.readline

num = input().strip()
cnt = Counter(num)
tmp = (cnt['6'] + cnt['9'] + 1) // 2
cnt['6'], cnt['9'] = tmp, tmp
print(max(cnt.values()))
