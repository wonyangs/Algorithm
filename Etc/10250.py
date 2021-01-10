# Solved on 2020.12.12
# 10250 ACM 호텔

N = int(input())  # 반복횟수 입력

for i in range(N):
    h, w, n = map(int, input().split())  # h : 높이, w : 호실개수, n : 손님번호

    if n % h == 0:  # n이 h의 배수일 경우
        print(h * 100 + n // h)
    else:
        print(n % h * 100 + n // h + 1)
