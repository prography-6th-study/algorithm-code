"""
정사각형이 늘어날 때마다 둘레가 dp[i] = dp[i-2] + dp[i-1] 의 규칙을 가지고 있는 것을 파악하고
해당 점화식을 통해 간단하게 구현
"""

def solution(N):
    dp = [0] * 81
    dp[0] = 4
    dp[1] = 6
    dp[2] = 10
    for i in range(3, N + 1):
        dp[i] = dp[i-2] + dp[i-1]
    return dp[N-1]