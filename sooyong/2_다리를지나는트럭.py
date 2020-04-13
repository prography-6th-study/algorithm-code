from collections import deque

def solution(bridge_length, weight, truck_weights):
    lenfirst = len(truck_weights)
    truck_weightsDQ = deque(truck_weights)
    time = 0
    curWeight = 0
    overed = []
    curSumWeight = 0
    bridge = deque([0 for i in range(bridge_length)], maxlen=bridge_length)

    while(True):
        time += 1
        curOutput = bridge.popleft()
        if curOutput != 0:
            overed.append(curOutput)
            curSumWeight -= curOutput
        if len(truck_weightsDQ) != 0 and curSumWeight + truck_weightsDQ[0] <= weight:
            curSumWeight += truck_weightsDQ[0]
            bridge.append(truck_weightsDQ.popleft())  
        else:
            bridge.append(0)
        if len(overed) == lenfirst:
            break
    return time
