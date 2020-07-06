import pytest


def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        count = 0
        for j in range(i+1, len(prices)):
            count += 1
            if prices[i] > prices[j]:
                break
        answer.append(count)
    answer.append(0)
    return answer

@pytest.mark.parametrize("prices, expected", [
    ([1, 2, 3, 2, 3], [4, 3, 1, 1, 0])
])
def test_simple(prices, expected):
    assert solution(prices) == expected

"""
[ 풀이 방법 ]
- 이중 for문을 돌면 되는거라고 생각했다. 스택/큐가 어디에 쓰이는거지?
"""