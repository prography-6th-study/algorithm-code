import pytest


def solution(N):
    dp = [1, 1] + [0] * (N - 1)
    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[-1] * 2 + dp[-2] * 2


@pytest.mark.parametrize(
    "N, expected", [(5, 26), (6, 42)],
)
def test_simple(N, expected):
    assert solution(N) == expected


"""
[ 풀이 방법 ]
    dp[i] = dp[i-1] + dp[i-2]가 쉽게 눈에 들어왔다.
    어렵지 않게 for문으로 구할 수 있었음
"""
