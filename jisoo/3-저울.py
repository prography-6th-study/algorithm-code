import pytest


def solution(weight):
    weight.sort()
    answer = 1
    for w in weight:
        if w > answer:
            break
        answer += w
    return answer
    


@pytest.mark.parametrize("weight, expected", [
    ([3, 1, 6, 2, 7, 30, 1], 21)
])
def test_simple(weight, expected):
    assert solution(weight) == expected

"""
[ 풀이 방법 ]
역시나 몰라서 인터넷을 찾아봤다...ㅎㅎㅎ
i번째까지 추들의 합을 누적해서 더한 값을 sum이라 할 때, i+1번째 원소가 sum +1 보다 크다면, 그 sum +1을 주어진 추로는 만들 수 없다. 

answer을 처음에 1로 설정하는게 중요했다.
"""