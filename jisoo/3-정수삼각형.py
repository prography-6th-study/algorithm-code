import pytest


def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == i:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    return max(triangle[-1])


@pytest.mark.parametrize("triangle, expected", [
    ([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]], 30)
])
def test_simple(triangle, expected):
    assert solution(triangle) == expected

"""
[ 풀이 방법 ]
- 숫자를 위에서 더해온 값으로 바꿔주면서 최댓값을 찾는다.
"""