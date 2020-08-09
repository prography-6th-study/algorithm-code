from math import gcd

import pytest


def solution(w, h):
    num = gcd(w, h)
    return w*h - (w+h-num)


@pytest.mark.parametrize("w, h, expected", [
    (8, 12, 80)
])
def test_simple(w,h, expected):
    assert solution(w,h) == expected

"""
[ 풀이 방법 ]
- 대각선으로 잘랐을 때 못쓰게 되는 정사각형이 몇개인지 어떻게 알까?
인터넷 검색해보니까 x축이 2의 배수일 때, y축이 3의 배수일 때 대각선이 꼭짓점에서 만난다고 한다.
(2,3), (4,6) ... -> 꼭짓점에서 만나는 경우

대각선이 꼭짓점을 만나는 만나는 개수는 w, h의 최대공약수이다.

대각선이 지나가는 박스의 크기는 (w/gcd) * (h/gcd)
대각선이 지나가는 정사각형 개수는 w+h-gcd
"""