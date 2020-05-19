"""
supplies 중 가장 큰 값만 공급 받으면, 최소 공급으로 버틸 수 있다. 
heapq는 기본적으로 최소힙만 지원을 하기 때문에
push할 때 -1를 곱하고, pop할 때 -1을 곱함으로써 최대힙을 구현할 수 있다. 
"""

import pytest
import heapq

def solution(stock, dates, supplies, k):
    answer = 0
    idx = 0
    heap = []
    while stock < k:
        for i in range(idx, len(dates)):
            if stock >= dates[i]:
                heapq.heappush(heap, (-supplies[i]))
                idx += 1
            else:
                break
        stock += (-heapq.heappop(heap))
        answer += 1
    return answer

@pytest.mark.parametrize("stock, dates, supplies, k, expected", [
    (4, [4, 10, 15], [20, 5, 10], 30, 2),
])
def test_simple(stock, dates, supplies, k, expected):
    assert solution(stock, dates, supplies, k) == expected