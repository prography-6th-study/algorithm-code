import pytest


def solution(m, n, puddles):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i==1 and j==1:
                dp[i][j] = 1
                continue
            if [j, i] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] += (dp[i-1][j] + dp[i][j-1]) % 1000000007
    print(dp)
    return dp[n][m] % 1000000007

@pytest.mark.parametrize("m, n, puddles, expected", [
    (4, 3, [[2, 2]], 4)
])
def test_simple(m, n, puddles, expected):
    assert solution(m, n, puddles) == expected

"""
[ 풀이 방법 ]
- 그냥 전체 경우의 수를 저장해놓으면서 마지막에 가장 작은 값을 return하면 될 것 같다
- 그냥 계속 값을 더해가면서 구하면 됐음. 왜 결국 가장 작은 값이 나오는지는 모르겠답...
"""