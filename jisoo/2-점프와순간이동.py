import pytest


def solution(n):
    count = 0
    while n > 0:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            count += 1
    return count


@pytest.mark.parametrize("n, expected", [
    ()
])
def test_simple(n, expected):
    assert solution(n) == expected

"""
[ 풀이 방법 ]
- 현재 n 값이 짝수이면 나누고 홀수면 -1 을 해가면 되는 문제였다...
"""