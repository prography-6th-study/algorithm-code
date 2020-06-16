"""
위쪽 대각선 오른쪽(dp[i-1][j-1]), 위쪽 대각선 왼쪽(dp[i-1][j]) 중
max를 이용하여 큰 값만 추출하고, 현재 위치의 값(triangle[i - 1][j - 1]) 을 더해주는 식으로 최대값을 찾음.
->  sum[i][j] = max(sum[i-1][j-1],sum[i-1][j]) + tri[i-1][j-1]

max(dp[i - 1][j - 1], dp[i - 1][j]) 에서 IndexError를 방지하기 위해서.. 배열 크기를 n+1 크기로 정의하고 가장 위쪽에 padding을 추가하였고,
실제 계산을 1부터 n+1까지(n번) 돌면서 계산하도록 구현하였다. 1부터 시작하기 때문에 triangle[i][j]가 아닌 triangle[i - 1][j - 1] 가 되었음.

최종적으로 dp를 출력해보면 아래와 같다.
[[0, 0, 0, 0, 0, 0], [0, 7, 0, 0, 0, 0], [0, 10, 15, 0, 0, 0], [0, 18, 16, 15, 0, 0], [0, 20, 25, 20, 19, 0], [0, 24, 30, 27, 26, 24]]
"""

def solution(triangle):
    n = len(triangle)
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i - 1][j - 1]
    return max(dp[-1])


t = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(t))