def solution(budgets, M):
    if (sum(budgets) <= M):
        return max(budgets)

    answer = 0
    upperLimit = 0
    maxLimit = max(budgets)

    while (upperLimit <= maxLimit):
        result = 0
        average = (upperLimit+maxLimit)//2
        for b in budgets:
            if average >= b:
                result += b
            else:
                result += average
        if result > M:
            maxLimit = average-1
        else:
            answer = average
            upperLimit = average+1
    return answer