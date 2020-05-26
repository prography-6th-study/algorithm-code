"""
원래 하려고 했던 방법은 가능한 모든 조합을 계산하는 방법이었는데, 당연히 실패했고..
의상을 입지 않는 것도 하나의 방법으로 칠 수 있다는 아이디어를 이용해 간단히 구현하였다.
"""

import pytest
from itertools import combinations

def solution_mine(clothes):
    d = dict()
    li = []
    mul_li = []
    ret = 0
    for clothes in clothes:
        if clothes[1] in d:
            d[clothes[1]] += 1
        else:
            d[clothes[1]] = 1
    keys = list(d.keys())
    for i in range(1, len(d) + 1):
        li.append(list(combinations(range(len(d)), i)))
    for cs in li:
        for c in cs:
            mul_li.append(''.join(map(str, c)))
    for mul in mul_li:
        v = 1 
        for i in range(len(mul)):
            v *= d[keys[int(mul[i])]]
        ret += v
    return ret

def solution(clothes):
    d = dict()
    for clothes in clothes:
        if clothes[1] in d:
            d[clothes[1]] += 1
        else:
            d[clothes[1]] = 1
    ret = 1
    for i in list(d.values()):
        ret *= (i + 1)
    return ret - 1

@pytest.mark.parametrize("clothes, expected", [
    ([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']], 5),
    ([['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']], 3)

])
def test_simple(clothes, expected):
    assert solution(clothes) == expected

solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']])
solution([['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']])