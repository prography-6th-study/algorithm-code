import pytest


def solution(d, budget):
    d.sort()
    total = 0
    answer = 0
    for n in d:
        total += n
        if total > budget:
            break
        answer += 1
    return answer


@pytest.mark.parametrize("d, budget, expected", [
    ([1, 3, 2, 5, 4], 9, 3)
])
def test_simple(d, budget, expected):
    assert solution(d, budget) == expected

"""
[ 풀이 방법 ]
- 
"""