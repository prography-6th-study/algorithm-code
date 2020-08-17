import pytest


def solution(s):
    s = list(s)
    answer = 0
    while len(s) > 0:
        answer = 0
        for s1, s2 in zip(s, s[1:]):
            if s1 == s2:
                s.remove(s1)
                s.remove(s2)
                answer = 1
        if answer == 0:
            break
    return answer


@pytest.mark.parametrize("s, expected", [
    ("baabaa", 1),
    ("cdcd", 0)
])
def test_simple(s, expected):
    assert solution(s) == expected

"""
[ 풀이 방법 ]
- 
"""