import pytest
from itertools import combinations


def solution(number, k):
    num = list(combinations(number, len(number)-k))
    m = max(num)
    
    return ''.join(m)



@pytest.mark.parametrize("number, k, expected", [
    # ("1924", 2, "94"),
    # ("1231234", 3, "3234"),
    ("4177252841", 4, "775841")
])
def test_simple(number, k, expected):
    assert solution(number, k) == expected

"""
[ 풀이 방법 ]
- combination을 이용해서 풀었더니 시간초과 발생
"""