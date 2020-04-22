import pytest
import heapq


def solution(stock, dates, supplies, k):
    temp = []
    answer = 0
    idx = 0
    while stock < k:
        for i in range(idx, len(dates)):
            # 재고가 떨어지기 전 경우만 생각
            if stock < dates[i]:
                break
            heapq.heappush(temp, -supplies[i])
            idx += 1
        stock += -heapq.heappop(temp)
        answer += 1
    return answer


@pytest.mark.parametrize("stock, dates, supplies, k, expected", [
    (4, [4, 10, 15], [20, 5, 10], 30, 2)
])
def test_simple(stock, dates, supplies, k, expected):
    assert solution(stock, dates, supplies, k) == expected


"""풀이 방법

현재 재고가 떨어지기 전에 temp에 받을 수 있는 재고 값을 넣어준다.
그 다음 heapq를 이용해서 최댓 값을 넣어준다

파이썬에서는 최소힙만 제공하기 때문에 -값으로 넣어주고, pop하면서 -해줬다.
"""
