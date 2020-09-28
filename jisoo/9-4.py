import pytest


def solution(a):
    # 열에 대한 1 개수
    one_count = [0 for _ in range(len(a[0]))]
    zero_count = 0
    for arr in a:
        for i in range(len(arr)):
            one_count[i] += arr[i]
    print(one_count)

    while True:


    


@pytest.mark.parametrize("a, expected", [
    ([[0, 1, 0], [1, 1, 1], [1, 1, 0], [0, 1, 1]], 6),
    ([[1, 0, 0], [1, 0, 0]], 0),
    ([[1, 0, 0, 1, 1], [0, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 1]], 72)
])
def test_simple(a, expected):
    assert solution(a) == expected

"""
[ 풀이 방법 ]
- 
"""