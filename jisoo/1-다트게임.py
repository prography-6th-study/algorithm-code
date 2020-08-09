import pytest


def solution(dartResult):
    for dart in dartResult:
        
    


@pytest.mark.parametrize("dartResult, expected", [
    ("1S2D*3T", 37),
    ("1D2S#10S", 9)
])
def test_simple(dartResult, expected):
    assert solution(dartResult) == expected

"""
[ 풀이 방법 ]
- 
"""