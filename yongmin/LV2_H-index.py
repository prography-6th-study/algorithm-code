def solution(citations):
    n = len(citations)  # 논문의 수
    citations.sort(reverse=True)

    answer = 0
    # h-index의 최대값은 n
    # n부터 1까지 반복하므로 처음 조건을 만족하는 것이 최대값
    for h in range(n, 0, -1):
        # h번 이상 인용된 논문의 수 구하기
        cited = 0
        for c in citations:
            if h <= c:
                cited += 1
            else:
                break

        # h번 이상 인용된 논문이 h편 이상 인용 and 나머지 논문이 h번 이하 인용
        if (h <= cited) and (n - cited) <= h:
            answer = h
            break

    return answer


print(solution([3, 0, 6, 1, 5]))