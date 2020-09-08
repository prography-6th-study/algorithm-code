import pytest


def solution(n, a, b):
    answer = 0
    while a != b:
        a = (a+1) // 2
        b = (b+1) // 2
        answer += 1

    return answer


@pytest.mark.parametrize("n, a, b, expected", [
    (8, 4, 7, 3)
])
def test_simple(n, a, b, expected):
    assert solution(n, a, b) == expected

"""
[ 풀이 방법 ]
- a, b에 +1을 하는 이유 -> 홀수 일 경우는 +1을 해야 함. 짝수인 경우에도 하게 된느데 어차피 //2를 해서 값에는 변화가 없다.
- 나누기 2를 하는 이유 -> 이기면서 줄어드는 사람을 나타낸다.
"""