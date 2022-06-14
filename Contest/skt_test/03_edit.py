from collections import defaultdict
from bisect import bisect_left

def solution(n, plans, clients):
    answer = []

    data = defaultdict(set)
    total_service = set()
    for plan in plans:
        plan_data = plan.split()
        total_service = total_service.union(plan_data[1:])
        data[int(plan_data[0])] = total_service
        print(total_service)
    
    data_key = sorted(data.keys())
    print(data_key)
    for i in range(len(clients)):
        client = clients[i].split()
        client_data = int(client[0])
        client_service = set(client[1:])

        for j in range(bisect_left(data_key, client_data), len(data.keys())):
            if client_data <= data_key[j]:
                if data[data_key[j]].issubset(client_service):
                    answer.append(j + 1)
                    break
        
        if len(answer) == i:
            answer.append(0)
        print(answer[i])

    return answer


# n = 5
# plans = ["100 1 3", "500 4", "2000 5"]
# clients = ["300 3 5", "1500 1", "100 1 3", "50 1 2"]
# print(solution(n, plans, clients))

n = 5
plans = []
clients = []
for i in range(1, 300000):
    string = str(i * 100) + ' ' + str(i * 2)
    plans.append(string)
for j in range(1, 300000):
    string = str(j * 110) + ' ' + str(j * 2)
    clients.append(string)
print(solution(n, plans, clients))
