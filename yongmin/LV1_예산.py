def solution(d, budget):
    d.sort()
    cnt = 0
    for v in d:
        if v > budget:
            break
        cnt += 1
        budget -= v
    return cnt

# 부서별 신청 금액을 정렬한 후 예산에서 하나씩 빼주면서 지원 횟수를 파악하는 방식으로 풀었다.

# test
print(solution([1, 3, 2, 5, 4], 9))
print(solution([2, 2, 3, 3], 10))