# Solved on 2022. 12. 17.
# 4358 생태학

from collections import defaultdict
import sys
input = sys.stdin.readline

dic = defaultdict(int)
count = 0
while True:
    name = input().strip()
    if not name:
        break
    dic[name] += 1
    count += 1
for name, cnt in sorted(dic.items()):
    print("%s %.4f"%(name, cnt/count * 100))

