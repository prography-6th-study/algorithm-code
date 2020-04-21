def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length
    weight_sum = 0

    while bridge:
        time += 1
        weight_sum -= bridge.pop(0)

        if truck_weights:
            if weight_sum + truck_weights[0] <= weight:
                weight_sum += truck_weights[0]
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)

    return time


#test
print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
