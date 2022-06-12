def solution(periods, payments, estimates):
    answer = [0, 0]
    people_num = len(periods)

    for i in range(people_num):
        now_rank = 0
        if 24 <= periods[i] < 60 and sum(payments[i]) >= 900000:
            now_rank = 1
        elif 60 <= periods[i] and sum(payments[i]) >= 600000:
            now_rank = 1
        
        next_rank = 0
        if 24 <= periods[i] + 1 < 60 and sum(payments[i][1:]) + estimates[i] >= 900000:
            next_rank = 1
        elif 60 <= periods[i] + 1 and sum(payments[i][1:]) + estimates[i] >= 600000:
            next_rank = 1
        
        if now_rank == 0 and next_rank == 1:
            answer[0] += 1
        if now_rank == 1 and next_rank == 0:
            answer[1] += 1

    return answer