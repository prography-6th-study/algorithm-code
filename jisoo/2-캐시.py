from collections import deque

import pytest


def solution(cacheSize, cities):
    queue = deque([])
    time = 0
    if cacheSize == 0 or cacheSize == len(cities):
        return len(cities)*5

    for city in cities:
        city = city.lower()
        if city in queue:
            queue.remove(city)
            time += 1
        else:
            if len(queue) >= cacheSize:
                queue.popleft()
            time += 5
        queue.append(city)
    return time

    


@pytest.mark.parametrize("cacheSize, cities, expected", [
    (3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"], 50),
    (3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"], 21),
    (0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"], 25),
    (2, ["Jeju", "Pangyo", "NewYork", "newyork"], 16),
    (5, ['seoul', 'seoul', 'seoul'], 7)
])
def test_simple(cacheSize, cities, expected):
    assert solution(cacheSize, cities) == expected

"""
[ 풀이 방법 ]
- 큐 문제 같음
"""