# Solved on 2022. 8. 10.
# 25372 성택이의 은밀한 비밀번호

import sys
input = sys.stdin.readline

print("\n".join('yes' if 6 <= len(n) <= 9 else 'no' for n in [input().strip() for _ in range(int(input()))]))
