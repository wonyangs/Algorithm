import sys

input = sys.stdin.readline

input()
c = 0
for l in sys.stdin:
    s = l.strip()
    if s == "고무오리 디버깅 끝":
        break
    if s == "고무오리":
        c = c - 1 if c else c + 2
    elif s == "문제":
        c += 1
print("고무오리야 사랑해" if not c else "힝구")
