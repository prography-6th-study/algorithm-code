import pytest


def solution(arrangement):
    count = 1
    answer = 0
    for i in range(1, len(arrangement)):
        if arrangement[i] == '(':
            count += 1
        else:
            count -= 1
            # 레이저인 경우
            if arrangement[i-1] == '(':
                answer += count
            # 막대기가 끝난 경우
            else:
                answer += 1
        
    return answer

@pytest.mark.parametrize("arrangement, expected", [
    ("()(((()())(())()))(())", 17)
])
def test_simple(arrangement, expected):
    assert solution(arrangement) == expected

"""
[ 풀이 방법 ]
- 괄호가 ()바로 이 모양이 나올 때 스택에 남은 '('개수가 잘리는 쇠막대기 개수라고 생각함
"""