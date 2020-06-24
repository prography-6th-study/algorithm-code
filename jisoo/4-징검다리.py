import pytest


def solution(distance, rocks, n):
    answer = 0
    rocks.append(distance)
    rocks.sort()
    
    left, right = 0, distance
    while left <= right:
        mid = (left+right)//2
        removed = 0
        prev = 0
        min_distance = []

        for rock in rocks:
            # 기준 거리보다 작은 경우
            if rock - prev < mid:
                removed += 1
            else:
                min_distance.append(rock-prev)
                prev = rock
        
        if removed > n:
            right = mid-1
        else:
            answer = min(min_distance)
            left = mid+1
    return answer

    


@pytest.mark.parametrize("distance, rocks, n, expected", [
    (25, [2, 14, 11, 21, 17], 2, 4)
])
def test_simple(distance, rocks, n, expected):
    assert solution(distance, rocks, n) == expected

"""
[ 풀이 방법 ]
- 이게 왜 이분탐색이지? 이분탐색으로 어떻게 풀어야하지... 너무 어렵다

- 바위 사이의 최소거리를 정해놓고 그 최소거리보다 작은 바위들을 제거하는 것
- 만약 제거하는 바위의 개수가 주어진 n보다 크면 거리를 더 좁히고 n보다 작으면 거리를 늘린다.
- 이 최소 거리를 찾는 방법을 이분탐색으로 하면 된다.
"""