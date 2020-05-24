import pytest
import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    # 최솟값이 K보다 크면 끝!
    while scoville[0] < K:
        # 스코빌 점수를 K이상 만들 수 없는 경우
        if len(scoville) < 2:
            return -1
        # 새로운 스코빌 점수 만들기
        new = heapq.heappop(scoville) + heapq.heappop(scoville)*2
        heapq.heappush(scoville, new)
        answer += 1
    return answer


@pytest.mark.parametrize("scoville, K, expected", [
    ([1, 2, 3, 9, 10, 12], 7, 2)
])
def test_simple(scoville, K, expected):
    assert solution(scoville, K) == expected


"""풀이 방법
가장 맵지 않은 -> heap을 이용해서 풀었다.
가장 맵지 않은 음식과 두번째 음식이니까 pop해서 값을 가져오고
결과를 계산해서 다시 넣어줬다.
"""
