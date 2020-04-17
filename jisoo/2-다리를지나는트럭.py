import pytest
from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length, maxlen=bridge_length)
    truck_weights = deque(truck_weights)
    current_weight = 0
    while truck_weights:
        # 다리 끝까지 간 트럭 빼주기
        if bridge[0] > 0:
            current_weight -= bridge[0]
            bridge.popleft()
        # 다리 위에 트럭 올리기
        if current_weight+truck_weights[0] <= weight:
            current_weight += truck_weights[0]
            bridge.append(truck_weights.popleft())
        # 트럭 밀어주기
        else:
            bridge.append(0)
        answer += 1
    # 남아있는 트럭 빼주기
    while bridge:
        bridge.pop()
        answer += 1
    return answer


@pytest.mark.parametrize("bridge_length, weight, truck_weights, expected", [
    (2,	10,	[7, 4, 5, 6], 8),
    (100, 100, [10], 101),
    (100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10], 110)
])
def test_simple(bridge_length, weight, truck_weights, expected):
    assert solution(bridge_length, weight, truck_weights) == expected


"""풀이 방법
다리 길이의 queue를 만든다.
그 다음 다리가 견딜 수 있는 무게면 트럭을 올린다
아닌 경우는 0을 더한다
트럭이 다리 끝에 와주면 pop을 통해 다리에서 꺼내준다.
트럭이 없을 떄 까지 반복한다.

처음에는 sum()을 통해서 계산했는데 시간 초과가 나와서
current_weight라는 변수로 다리 위에 무게를 계산해 줬더니 통과했다.
"""
