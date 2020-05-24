import pytest


def solution(numbers, target):
    def dfs(idx):
        if idx == len(numbers):
            if sum(numbers) == target:
                global answer
                answer += 1
                print(numbers)
            return answer
        dfs(idx + 1)
        numbers[idx] *= -1
        dfs(idx + 1)

    global answer
    answer = 0
    dfs(0)
    return answer


@pytest.mark.parametrize(
    "numbers, target, expected", [([1, 1, 1, 1, 1], 3, 5)],
)
def test_simple(numbers, target, expected):
    assert solution(numbers, target) == expected


"""
[ 풀이 방법 ]
    dfs문제라고 생각햇다.
    깊게 내려가면서 결과를 확인하면 될 것 같다

    재귀로 푼 이유는 +, -를 아예 다른 경우로 생각해야 하기 때문
"""
