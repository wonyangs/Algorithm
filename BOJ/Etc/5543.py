# Solved on 2022. 5. 21.
# 5543 상근날드

import sys
input = sys.stdin.readline

print(min([int(input())for _ in range(3)])+min([int(input())for _ in range(2)])-50)
