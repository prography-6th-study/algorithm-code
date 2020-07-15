import pytest

from itertools import permutations
import re


def solution(expression):
    math = list(permutations(['+', '-', '*'], 3))
    print(math)
    expression = expression.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').split(' ')
    print(expression)
    for ma in math:
        temp = expression
        for m in ma:
            for idx, t in enumerate(temp):
                if t == m:
                    st = temp[idx-1]+temp[idx]+temp[idx+1]
                    print(m, st)
                    num = eval(st)
                    print(num)



@pytest.mark.parametrize("expression, expected", [
    ("100-200*300-500+20", 60420),
    ("50*6-3*2", 300)
])
def test_simple(expression, expected):
    assert solution(expression) == expected

"""
[ 풀이 방법 ]
- 
"""