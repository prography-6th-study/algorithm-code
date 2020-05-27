"""
budgets 배열 중 max 값을 기준으로 하여 최대값(테스트케이스 기준 0~150 중의 값 중에 조건을 만족하는 최대값)을 이분 탐색으로 찾음.
brute-force로 접근하기에는 시간 초과 위험이 있기 때문에, 이분 탐색을 이용해야 시간 내에 문제를 해결할 수 있다.
"""

def solution(budgets, M):
    budgets.sort()
    start = 0
    end = max(budgets)
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for ele in budgets:
            if ele <= mid:
                total += ele
            else:
                total += mid
        if total < M:
            start = mid + 1
            limit = mid
        else:
            end = mid - 1 
    return limit

budgets = [120, 110, 140, 150]
M = 485

print(solution(budgets, M))