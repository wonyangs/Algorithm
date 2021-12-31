# Solved on 2020.12.12
# 2798 블랙잭

n, m = map(int, input().split())  # n : 카드의 개수, m : 기준이 될 수

a = sorted(list(map(int, (input().split()))))  # 카드를 담을 리스트를 정렬해서 저장

s = set()  # 합계를 담을 집합

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            csum = a[i] + a[j] + a[k]
            if csum <= m:  # m 이하인 값만 추가
                s.add(csum)
                break

print(max(s))  # m 이하인 합들 중 최댓값 출력
