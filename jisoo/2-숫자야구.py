import pytest
from itertools import permutations


def solution(baseball):
    # 모든 경우의 수 만들어주기
    candidate = list(permutations(['1', '2', '3', '4', '5', '6', '7', '8', '9'], 3))
    candidate = list(map(''.join, candidate))
    for n, strike, ball in baseball:
        n = str(n)
        temp = []
        for c in candidate:
            s, b = 0, 0
            for i in range(3):
                if c[i] == n[i]:
                    s += 1
                elif n[i] in c:
                    b += 1
            if s == strike and b == ball:
                temp.append(c)

        candidate = temp
    return len(candidate)


@pytest.mark.parametrize("baseball, expected", [
    ([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]], 2)
])
def test_simple(baseball, expected):
    assert solution(baseball) == expected

"""
[ 풀이 방법 ]
    - 재귀로 모든 경우를 따지면 된다고 생각함
    - 찾아보니 모든 경우의 수를 만들어 놓고 지워가면 되는 거였다.

    - ball, strike가 되는 경우를 남기고 아닌 경우를 지운다.
    - 처음에는 일치하는 숫자를 찾으면 된다고 생각했다.
    - 그것보다는 각 숫자의 strike, ball을 계산해서 일치하면 넣어주는 방법이 좋은 것 같다.
"""