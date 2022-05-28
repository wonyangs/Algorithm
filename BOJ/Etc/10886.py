# Solved on 2022. 5. 29.
# 10886 0 = not cute / 1 = cute

import sys
input = sys.stdin.readline

N = int(input())
cute = 0
ncute = 0
for _ in range(N):
    if int(input()) == 0:
        ncute += 1
    else:
        cute += 1
print("Junhee is cute!" if cute > ncute else "Junhee is not cute!")
