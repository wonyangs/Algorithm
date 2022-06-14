from collections import defaultdict
from bisect import bisect_left

def solution(n, plans, clients):
    answer = []
    data = []
    service = [-1] * (n + 1)

    for i in range(len(plans)):
        arr = [*map(int, plans[i].split())]
        data.append(arr[0])
        for j in arr[1:]:
            service[j] = i
    
    for client in clients:
        arr = [*map(int, client.split())]
        data_min = bisect_left(data, arr[0])
        service_min = -1
        is_service = 1
        for j in arr[1:]:
            if service[j] == -1:
                is_service = 0
                break
            service_min = max(service_min, service[j])
        if is_service:
            answer.append(max(data_min, service_min) + 1)
        else:
            answer.append(0)

    return answer


# n = 5
# plans = ["100 1 3", "500 4", "2000 5"]
# clients = ["300 3 5", "1500 1", "100 1 3", "50 1 2"]
# print(solution(n, plans, clients))

n = 300000
plans = []
clients = []
for i in range(1, 300000):
    string = str(i * 100) + ' ' + str(i)
    plans.append(string)
for j in range(1, 300000):
    string = str(j * 110) + ' ' + str(j)
    clients.append(string)
print(solution(n, plans, clients))
