""" 
너무 복잡하게 푼 것 같다.
cnt를 처음에는 [0] * len(bridge_length)로 선언하여 풀려고 했는데,
index 확인이 어려워서 dependency가 아예 동일하게 q와 cnt를 둘다 deque()로 통일시켜 풀었다.
"""

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = deque() # 다리를 건너는 트럭 queue
    cnt = deque() # 다리 위에서 몇 초나 있었는지 확인하는 queue - dependency가 q와 동일함
    truck_weights = deque(truck_weights) # 대기트럭 queue
    while True:
        if len(truck_weights) == 0 and len(q) == 0:
            break
        for i in range(len(q)):
            cnt[i] += 1
        if len(q) != 0:
            if cnt[0] == bridge_length:
                q.popleft()
                cnt.popleft()
        if len(truck_weights) != 0:
            if truck_weights[0] + sum(q) <= weight:
                q.append(truck_weights.popleft())
                cnt.append(0)
        answer += 1
    return answer