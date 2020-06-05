import pytest
import heapq


def solution(operations):
    heap = []

    for oper in operations:
        o, n = oper.split()
        if o == 'I':
            heapq.heappush(heap, int(n))
            continue
        if not heap:
            continue
        if n == '1':
            heap.sort()
            heap.pop()
        else:
            heapq.heappop(heap)
    if heap:
        heap = [max(heap), min(heap)]
        return heap
    return [0, 0]
    


@pytest.mark.parametrize("opertaions, expected", [
    (["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"], [0, 0]),
    (["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"], 	[333, -45])
])
def test_simple(opertaions, expected):
    assert solution(opertaions) == expected

""" [풀이 방법]
- 최댓값을 꺼내야 하는 경우에는 그냥 리스트 정렬해서 pop 해줬음
- 최솟값은 파이썬 heapq를 이용해서 꺼내줌
"""