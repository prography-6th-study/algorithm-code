# 예산
def solution(budgets, M):
    answer = 0
    # 상한액은 1 ~ 각 지역 요청의 최대값 사이
    low, high = 1, max(budgets)

    # 이분탐색으로 상한액 찾기
    while low <= high:
        mid = (low + high) // 2 # 예산 상한액
        total = 0 # 예산 총합

        # mid를 상한액으로 설정하고 예산총합을 계산
        for budget in budgets:
            if budget < mid:
                total += budget
            else:
                total += mid

        # 조건을 만족한다면 mid 이상의 범위에서 다시 찾는다
        if total < M:
            low = mid + 1
            answer = mid
        else: # 조건을 만족하지 못하면 mid 이하의 범위에서 다시 찾는다
            high = mid - 1

    return answer


# test
print(solution([120, 110, 140, 150], 485))