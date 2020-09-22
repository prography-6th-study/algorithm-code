import pytest


def solution(a):
    length = len(a)

    min_left = a[0]
    check = [False] * length

    for idx in range(1, length-1):
        if a[idx] < min_left:
            min_left = a[idx]
            check[idx] = True

    min_right = a[-1]
    for idx in range(length-1, 1, -1):
        if a[idx] < min_right:
            min_right = a[idx]
            check[idx] = True

    answer = sum(1 for c in check if c is True) + 2
    return answer



@pytest.mark.parametrize("a, expected", [
    ([9,-1,-5], 3),
    ([-16,27,65,-2,58,-92,-71,-68,-61,-33], 6)
])
def test_simple(a, expected):
    assert solution(a) == expected

"""
[ 풀이 방법 ]
- 현재 위치의 왼쪽 오른쪽 비교 -> 
자기 왼쪽, 오른쪽  다 죽여줄 수 있는지 아닌지??
한쪽이라도 내가 다 이길 수 있는건 이긴다 -> 나보다 큰 수는 이긴다
둘다 지는 상황이면 진다

양 끝은 무조건 이길 수 있음
"""