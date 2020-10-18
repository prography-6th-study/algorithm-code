import pytest


def change_base(n, base=3):
    base_num = []
    while n > base-1:
        base_num.append(n % base)
        n = n//base
    base_num.append(n)
    return ''.join(map(str, base_num))


def solution(n):
    return int(change_base(n), 3)


@pytest.mark.parametrize("n, expected", [
    (45, 7),
    (125, 229)
])
def test_simple(n, expected):
    assert solution(n) == expected

"""
[ 풀이 방법 ]
- 
"""