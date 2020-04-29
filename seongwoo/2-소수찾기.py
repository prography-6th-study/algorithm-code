"""
에라토스테네스의 체를 이용해서 구현
"""

import pytest
from itertools import permutations

def prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, round(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    cnt = 0
    ret = []
    for i in range(1, len(numbers) + 1):
        for each_tuple in list(set(permutations(numbers, i))):
            ret.append(int(''.join(each_tuple)))
    print(ret)
    for i in list(set(ret)):
        if prime(i) == True:
            cnt += 1
    return cnt

@pytest.mark.parametrize("numbers, expected", [
    ("17", 3),
    ("011", 2),
    ("2", 1),
    ("7843", 12)
])
def test_simple(numbers, expected):
    assert solution(numbers) == expected
