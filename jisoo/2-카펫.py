import pytest


def solution(brown, yellow):
    for i in range(1, yellow+1):
        if yellow%i == 0:
            j = yellow//i
            if (i+2) * (j+2) - yellow == brown:
                return [max(i+2, j+2), min(i+2, j+2)]


@pytest.mark.parametrize("brown, yellow, expected", [
    (10, 2, [4, 3]),
    (8, 1, [3, 3]),
    (24, 24, [8, 6])
])
def test_simple(brown, yellow, expected):
    assert solution(brown, yellow) == expected

""" [ 풀이방법 ]
노란색 상자의 크기를 구하면 거기서 +2 를 해주면 전체 가로, 세로 길이를 구할 수 있다
"""