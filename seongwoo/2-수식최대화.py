"""
기본 테스트케이스는 통과하고 나머지는 1/10만 통과하는데 뭐가 문제인지 잘 모르겠다 ㅠㅠ
while 쪽이 문제인 것 같긴한데 낼까지 좀 더 생각해봄..

접근 방식은 연산자와 피연산자로 나누고,
deque의 rotate를 이용해 연산자 우선순위를 변경해가면서
계산한 값의 절댓값이 가장 값이 큰 경우에 갱신하는 식으로 풀었슴다..

"""


import pytest
from collections import deque

def solution(expression):
    result = float('-inf')
    operand = expression.replace('+', '/').replace('-', '/').replace('*', '/').split('/')  # ['100', '200', '300', '500', '20']
    operator = {'*','+','-'}
    op = []
    for o in list(operator):
        if o not in expression:
            operator -= set(o) # 사용되는 연산자만
    for o in expression:
        if o in operator:
            op.append(o) # ['-', '*', '-', '+']

    q = deque(operator)
    for _ in range(len(q)):
        q.rotate()
        operands = operand[:]
        ops = op[:]
        while len(operands) != 1:
            for o in q:
                for idx, i in enumerate(ops):
                    if i == o:
                        ret = operands[idx] + o + operands[idx + 1]
                        operands[idx] = str(eval(ret))
                        operands.pop(idx + 1)
                        ops.pop(idx)
        result = max(result, abs(int(operands[0])))
    return result

@pytest.mark.parametrize("expression, expected", [
    ("100-200*300-500+20", 60420),
    ("50*6-3*2"	, 300),

])
def test_simple(expression, expected):
    assert solution(expression) == expected