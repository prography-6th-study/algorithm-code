import pytest
from itertools import permutations

def solution(expression):
    result = float('-inf')
    operator = {'+', '-', '*'}
    operand = list(map(int, expression.replace('+', '/').replace('-', '/').replace('*', '/').split('/')))
    op = []
    for o in list(operator):
        if o not in expression:
            operator -= set(o) 
    for o in expression:
        if o in operator:
            op.append(o)

    for combi in list(permutations(operator, len(operator))):
        operands = operand[:]
        ops = op[:]
        for c in combi :
            i = 0
            while(len(operands) > 1 and c in ops) :
                o = ops[i]
                if o == c:
                    ops.pop(i)
                    n1, n2 = operands[i:i + 2]
                    del operands[i:i + 2]
                    if c == '+' : operands.insert(i, n1 + n2)
                    elif c == '-' : operands.insert(i, n1 - n2)
                    else : operands.insert(i, n1 * n2)
                else: i += 1
        result = max(result, abs(operands[0]))
    return result

@pytest.mark.parametrize("expression, expected", [
    ("100-200*300-500+20", 60420),
    ("50*6-3*2"	, 300),

])
def test_simple(expression, expected):
    assert solution(expression) == expected
