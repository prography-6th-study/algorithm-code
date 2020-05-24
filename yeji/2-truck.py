def solution(bridge_length, weight, truck_weights):
    que = [0] * bridge_length
    answer = 0
    while(que):
        answer += 1
        que.pop(0)
        if truck_weights:
            if sum(que) + truck_weights[0] <= weight:
                que.append(truck_weights.pop(0))
            else:
                que.append(0)
    return answer