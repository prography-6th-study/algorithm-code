"""
heap에 push가 되면 자동으로 정렬이 됨을 활용하여
heap의 최소값이 K보다 크거나 같을 때, while문을 돈 횟수를 반환.
효율성 테스트는 몇몇에서 2000ms에 가까운 값이 나올 정도로 간신히 통과했다. 
"""

import pytest
import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)
    while True:
        if len(heap) == 1:
            break
        heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)
        answer += 1
        if heap[0] >= K:
            return answer
    return -1

@pytest.mark.parametrize("scoville, K, expected", [
    ([1, 2, 3, 9, 10, 12], 7, 2),
])
def test_simple(scoville, K, expected):
    assert solution(scoville,K) == expected