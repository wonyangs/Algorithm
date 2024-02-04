for _ in range(int(input())):
    total_cnt = 0
    total_grade = 0
    for __ in range(int(input())):
        cnt, grade = map(float, input().split())
        total_cnt += cnt
        total_grade += cnt * grade
    print("%d %.1f"%(total_cnt, total_grade / total_cnt))
