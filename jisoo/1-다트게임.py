import pytest


def solution(dartResult):
    answer = []
    num = 0
    for idx, dart in enumerate(dartResult):
        if dart == 'S':
            answer.append(num)
        elif dart == 'D':
            answer.append(num**2)
        elif dart == 'T':
            answer.append(num**3)
        elif dart == '*':
            answer[-1] = answer[-1]*2
            try:
                answer[-2] = answer[-2]*2
            except:
                pass
        elif dart == '#':
            answer[-1] = answer[-1]*-1
        else:
            num = int(dart)
            if dart == '0' and dartResult[idx - 1] == '1':
                num = 10
    return sum(answer)

        
    


@pytest.mark.parametrize("dartResult, expected", [
    ("1S2D*3T", 37),
    ("1D2S#10S", 9)
])
def test_simple(dartResult, expected):
    assert solution(dartResult) == expected

"""
[ 풀이 방법 ]
- s, d, t에 해당하는 점수를 계산한다
 - 바로 직전 숫자를 넣어줬더니 두자리 수는 처리가 안
- 상 받은 경우를 계산한다
"""