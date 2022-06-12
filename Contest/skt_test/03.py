from collections import defaultdict

def solution(n, plans, clients):
    answer = []

    data = defaultdict(set)
    total_service = set()
    for plan in plans:
        plan_data = plan.split()
        total_service = total_service.union(plan_data[1:])
        data[int(plan_data[0])] = total_service
    
    data_key = sorted(data.keys())
    for i in range(len(clients)):
        client = clients[i].split()
        client_data = int(client[0])
        client_service = set(client[1:])

        for j in range(len(data.keys())):
            if client_data <= data_key[j]:
                if len(client_service - data[data_key[j]]) == 0:
                    answer.append(j + 1)
                    break;
        
        if len(answer) == i:
            answer.append(0)

    return answer