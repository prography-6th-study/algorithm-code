import pytest


def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if i == j:
                continue
            answer.append(numbers[i]+numbers[j])
    answer = list(set(answer))
    answer.sort()
    return answer


@pytest.mark.parametrize("numbers, expected", [
    ()
])
def test_simple(numbers, expected):
    assert solution(numbers) == expected

"""
[ 풀이 방법 ]
- 
"""