"""
현재 배열의 위쪽 경우의 수(dp[i-1][j]) 와 왼쪽 경우의 수(dp[i][j-1]) 를 더해주면
해당 위치까지의 경우의 수가 나오는 것을 이용하여 구현하였음. 

처음 구현은 n*m 크기의 dp 배열을 선언하고 i==0 or j==0인 경우에 경우의 수를 1로 초기화하고 시도하였으나, 
(i==0 or j ==0) and ([j, i] in puddles)의 조건에서 i+1, j+1 이상의 위치들에 대해 
경우의 수를 0으로 초기화시키는 것에서 막혀 실패하였음.

이후 (n+1)*(m+1) 크기로 위쪽, 왼쪽에 0의 값을 가진 padding을 추가하여 위 문제를 해결하였다.
"""

def solution(m, n, puddles):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    dp[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            elif [j, i] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1] % 1000000007