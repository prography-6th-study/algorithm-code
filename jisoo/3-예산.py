def solution(budgets, M):
    if sum(budgets) < M:
        return max(budgets)

    budgets.sort()
    left = 0
    right = budgets[-1]
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        temp = [mid if x > mid else x for x in budgets]
        if sum(temp) <= M:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return answer


"""
[ 풀이방법 ]
    - 중간값을 최대 예산으로 했을 때 합계가 어떤지 확인한다.
    - left, right이 동일해지면 while문을 멈춘다.
"""
